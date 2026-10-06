Create your first Python sandbox
================================

In this tutorial you will create a Python sandbox in GRiPO. A sandbox is an isolated container where your code runs, separate from your other workflows and sandboxes. You will follow one short path and finish with a sandbox that is ready to use. It takes a few minutes.

You do not need any experience with sandboxes. Every choice in this tutorial is a safe default. If you want to know why a setting exists, each step links to the explanation. If you want the full list of options, see :doc:`../reference/sandbox-settings`.

What you need
-------------

* Access to a GRiPO workspace.

Step 1: Open the sandbox list
-----------------------------

In the left hand menu, click **Sandbox**. Then click **Create Sandbox** in the top right corner.

.. image:: ../images/01-sandbox-list.png
   :alt: The Available Sandboxes list with the Create Sandbox button in the top right

You should now see the creation wizard. It lists five steps on the left, and **Basic Information** is the first one.

Step 2: Fill in the basic information
-------------------------------------

Fill in the form like this:

* **Name:** ``Pythonsandbox``
* **Description:** ``Sandbox for running python commands and code``
* **Type:** ``Code``
* **Language:** ``Python``

The **Language** field appears after you choose a type. Leave **Time (seconds)**, **Backend** and **Worker Limit** as they are.

.. image:: ../images/02-basic-information.png
   :alt: The Basic Information step filled in for a Python sandbox

Scroll down to **Logo**. Type ``python`` in the search box and click an icon, for example ``FaPython``. The logo is only the picture shown next to your sandbox in the list.

.. image:: ../images/03-logo-selection.png
   :alt: Searching for a Python icon in the Logo section

You should now see your chosen icon in a preview box. Click **Next**.

Step 3: Choose an image
-----------------------

Select **Predefined (Our Images)**. GRiPO picks a suitable Python environment for you, based on the type and language you chose. To learn what the other options do, see :doc:`../reference/sandbox-settings`.

You should now see **Predefined (Our Images)** selected. Click **Next**.

Step 4: Check the resources
---------------------------

You do not need to change anything here. Check that the form shows these values:

* **User:** ``User``
* **Privileged:** ``False``

These settings keep your sandbox restricted. To find out why, see :doc:`../explanation/sandbox-security-and-isolation`.

.. image:: ../images/05-resources.png
   :alt: The Resources step with User and Privileged set to their safe values

You should now see **Concurrency**, **RAM (MB)** and **CPU (%)** already filled in. Click **Next**.

Step 5: Skip the rest and create the sandbox
--------------------------------------------

The next step is **Environment**. It shows the message "No environment variables set for this sandbox." You can skip it, so click **Next**.

.. image:: ../images/06-environment-variables.png
   :alt: The Environment step with no variables set

The last step is **Advanced**. Leave everything as it is and click **Create Sandbox**.

.. image:: ../images/08-advanced-bottom.png
   :alt: The Advanced step with the Create Sandbox button

Step 6: Check your sandbox
--------------------------

GRiPO returns you to the sandbox list.

You should now see **Pythonsandbox** in the list, with the type ``code``, the language ``python`` and **Built-in** set to ``No``. When the sandbox is ready, its **Status** shows ``running``.

You have created your first Python sandbox.

Where to go next
----------------

* To run your sandbox on a particular Python version, see :doc:`../howto/use-a-specific-python-version`.
* To give your code an API key without writing it into the code, see :doc:`../howto/add-an-environment-variable`.
* For every setting in the wizard, see :doc:`../reference/sandbox-settings`.