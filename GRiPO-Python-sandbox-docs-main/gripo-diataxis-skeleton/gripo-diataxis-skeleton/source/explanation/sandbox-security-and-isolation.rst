Sandbox security and isolation
==============================

A sandbox is a place where code can run without being trusted. That is the whole idea. You might run a script someone else wrote, a script you wrote in a hurry, or code that handles a secret. If something goes wrong, the damage should stay inside the sandbox.

Most of the settings in the creation wizard exist to decide how tight that boundary is. This page explains what the boundary protects, what each setting trades away, and how to think about the choices. For exact values and defaults, see :doc:`../reference/sandbox-settings`. To create a sandbox with the safe defaults, follow :doc:`../tutorials/create-your-first-python-sandbox`.

What isolation protects
-----------------------

A sandbox runs as its own container, separate from your other sandboxes, your workflows and GRiPO itself. A mistake inside one sandbox does not spread to the others. A script that crashes, fills its memory or loops forever affects only the sandbox it runs in.

Isolation does not make the code inside harmless. The code still does what it is told, and it can still use anything you give it, such as an API key. The boundary limits how far a problem can travel. It does not stop the problem from happening.

It helps to think of two separate questions. How far can a problem spread beyond the sandbox? And how much can it do inside the sandbox? The settings below answer one or both.

Limits that contain mistakes
----------------------------

Not every problem is an attack. Most are ordinary bugs. A script that waits forever, reads a file far larger than expected or starts too many processes can cause real trouble.

The time, memory, CPU and concurrency limits contain these bugs. A time limit makes a stuck script fail quickly instead of holding resources for as long as it likes. A memory limit means a runaway script crashes alone instead of slowing everything else down. The cost is that limits set too low cut off legitimate work. A script that processes a large file may be stopped halfway through.

This is why the sensible approach is to set limits a little above what your code normally needs. Very generous limits protect nothing, and very tight limits break working code.

User or Root
------------

By default a sandbox runs as a restricted user. That account can run scripts, read and write files, call APIs and install ordinary packages. It cannot change the system itself.

Root is the alternative. It has full administrative access inside the container. Some jobs need it, such as installing certain system level packages or changing system configuration. Most scripts do not.

The reason to prefer the restricted user is simple. If code runs as Root and something goes wrong, whether through a bug or through a malicious package, the problem has far more power over the container. The restricted user means a compromised script can do less. The trade off is convenience, because a few tasks will fail until you choose Root. That failure is useful information. If a task truly needs Root, you will know why you are granting it.

Privileged mode
---------------

Privileged mode goes further than Root. Root affects what the code can change inside the container. Privileged mode affects how much of the machine outside the container the code can reach.

With the Docker backend, a privileged container receives broad capabilities that ordinary containers do not have. It can access host hardware devices and run containers of its own. That is what makes it useful for specialised jobs such as running Docker inside Docker.

It is also why privileged mode is off by default. It removes much of the separation that makes a sandbox safe. A problem inside a privileged sandbox has a realistic path to the surrounding system, not just to the container. Treat it as something you enable for a specific technical need, and leave it off otherwise.

Security options add another layer. They apply operating system level restrictions to the container, independently of the User and Privileged settings. The idea is defence in depth. If one protection fails, another may still hold.

Keeping access to a minimum
---------------------------

SSH access is off by default for a related reason. Every way into a sandbox is one more thing that has to be secured. Without SSH, you reach the sandbox only through GRiPO, through its built in terminal or through workflows. Turning SSH on is reasonable when you need to debug interactively. It is worth turning off again when you no longer do.

Choosing an image
-----------------

The image decides what is installed before your code runs, and that matters for security as well as convenience. You are trusting whoever built the image.

Predefined images are the simplest choice. GRiPO picks one that matches your type and language, so there is nothing to evaluate.

Custom images from Docker Hub give you more control, such as a specific Python version. The search results show a star count and a pull count. Official images are maintained as part of Docker's own library and are widely used, so they are usually well tested and kept up to date. High numbers are a useful signal, but they are not a guarantee of safety. A little known community image may work perfectly well, or it may be out of date, missing tools or worse. Without a specific reason to choose one, an official or widely used image is the safer pick.

A Dockerfile gives complete control, because you define everything. The cost is effort and responsibility. The image has to be built before the sandbox starts, and you are accountable for what goes into it. It makes sense once the other options cannot give you what you need.

Why secrets stay out of your code
---------------------------------

If you write an API key directly into a script, everyone who can read the script can read the key. If the code ends up somewhere public, so does the key. Environment variables keep the value separate from the code, so you can share, review and version the code without exposing the secret.

This does not make a secret invisible. Code running in the sandbox can read the variables it is given, so a malicious script could read and misuse them. Environment variables solve the problem of secrets leaking through the code itself. They do not remove the need to give a sandbox only the credentials it truly needs. To add a variable, see :doc:`../howto/add-an-environment-variable`.

Temporary and persistent storage
--------------------------------

A sandbox starts clean every time. Files that it creates are lost when it stops or restarts. That is a feature for isolation, because nothing stale or unexpected carries over from one run to the next.

A volume changes that by attaching persistent storage. It is the right choice when your code builds up data over time, caches downloads or needs to keep state between runs. The trade off is that whatever is stored there outlives the sandbox, including mistakes and sensitive data. Use a volume when you need persistence, and not as a default.

The trade offs in short
-----------------------

The defaults in the wizard all lean the same way. They give the sandbox the least power that still lets ordinary code run. Each step away from them, such as Root, Privileged, SSH, a community image or a volume, buys capability at the price of a larger surface to defend.

That does not mean the defaults are always right. A sandbox that needs system packages needs Root, and one that builds Docker images needs more than the defaults allow. The aim is to make that a deliberate choice for a specific reason, instead of an accident.

Related
-------

* To create a sandbox with the safe defaults: :doc:`../tutorials/create-your-first-python-sandbox`.
* To choose a specific Python version through a custom image: :doc:`../howto/use-a-specific-python-version`.
* For exact values and defaults: :doc:`../reference/sandbox-settings`.