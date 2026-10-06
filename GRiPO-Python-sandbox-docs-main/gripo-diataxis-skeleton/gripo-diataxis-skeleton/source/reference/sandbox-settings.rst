Sandbox settings
================

This page lists every setting in the sandbox list and the sandbox creation wizard, in the order the product shows them. It states what each setting controls and the values it accepts. For a guided walkthrough, see :doc:`../tutorials/create-your-first-python-sandbox`. For the reasoning behind the security settings, see :doc:`../explanation/sandbox-security-and-isolation`.

The creation wizard has five steps: Basic Information, Image, Resources, Environment and Advanced. Fields marked as required must be filled in before you can continue.

Sandbox list
------------

The sandbox list is the **Sandbox** page in the left hand menu. It shows every sandbox in your workspace.

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Column
     - Description
   * - Name
     - The name given to the sandbox, shown with its logo.
   * - Type
     - The sandbox type. See `Sandbox types`_.
   * - Language
     - The programming language or runtime of the sandbox.
   * - Status
     - Whether the sandbox is running or stopped.
   * - Built-in
     - ``Yes`` if GRiPO created the sandbox automatically. ``No`` if a person created it.
   * - Updated
     - When the sandbox was last changed. The list is sorted by this column, newest first.
   * - Created
     - When the sandbox was created.
   * - Terminal
     - Opens a live terminal inside the sandbox.
   * - Action
     - A menu for editing, duplicating or deleting the sandbox.

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Control
     - Description
   * - Sandbox and Volume tabs
     - Switch between the list of sandboxes and the list of volumes.
   * - Search by name
     - Filters the list by sandbox name.
   * - All Types
     - Filters the list by sandbox type.
   * - Refresh
     - Reloads the list.
   * - Manage columns
     - Chooses which columns are shown.
   * - Create Sandbox
     - Starts the creation wizard.

Step 1: Basic Information
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 45 35

   * - Setting
     - What it controls
     - Values and default
   * - Name (required)
     - The label used to identify the sandbox in the sandbox list.
     - Text. Empty by default. Each sandbox needs a unique name.
   * - Description (required)
     - A short statement of the sandbox's purpose.
     - Text. Empty by default.
   * - Type
     - The fundamental behaviour of the sandbox. The fields in the rest of the form depend on the type.
     - One of the types listed under `Sandbox types`_.
   * - Language
     - The language or runtime the sandbox uses. It also determines the image that Predefined selects in Step 2.
     - Depends on the selected Type. The field is labelled *type dependent* in the product.
   * - Time (seconds)
     - The maximum execution time allowed for a single run in the sandbox.
     - Number of seconds. Default ``100``.
   * - Backend
     - The execution engine that runs the sandbox container.
     - ``Docker``.
   * - Worker Limit
     - The number of workers, meaning parallel execution processes, that the sandbox can use at once.
     - Number. Default ``1``.
   * - Logo (required)
     - The image shown next to the sandbox in the sandbox list. It has no effect on how the sandbox runs.
     - One of three modes: **Icon**, **Link** or **Initial**. See `Logo modes`_.

Sandbox types
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Type
     - Purpose
   * - Code
     - Runs application logic and scripts directly, such as Python, JavaScript or Bash.
   * - Custom
     - Tailored or specialised setups that do not fit the other types, often built around a custom Docker image.
   * - SSH
     - Secure remote terminal access to a server, for command line administration.
   * - Kubectl
     - Interacting with and managing Kubernetes clusters.
   * - Cloud Code
     - Direct interaction with cloud provider services and integrations.

Logo modes
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Mode
     - Description
   * - Icon
     - Search the icon library by name and select an icon, for example ``FaPython`` or ``FaAws``. A preview of the selected icon is shown.
   * - Link
     - Use an image from a URL.
   * - Initial
     - Use a single letter.

Step 2: Image
-------------

The Image step decides which software environment the sandbox starts with. Choose one of three options.

.. list-table::
   :header-rows: 1
   :widths: 25 45 30

   * - Option
     - What it does
     - Notes
   * - Predefined (Our Images)
     - Selects an image automatically from the Type and Language chosen in Step 1.
     - Marked **Recommended** in the product.
   * - Custom (Search Docker Hub)
     - Searches public images on Docker Hub. You pick an image and a tag.
     - See `Docker Hub image search`_.
   * - Dockerfile
     - You write or upload a Dockerfile. The image is built before the sandbox starts.
     - Marked **New** in the product.

Docker Hub image search
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Element
     - Description
   * - Docker Hub Image (required)
     - A search box for public Docker Hub images.
   * - Image filter
     - A drop down next to the search box. It is set to **All images** by default.
   * - Search results
     - Each result shows the image name, a short description, a star count and a pull count.
   * - Tag
     - The version of the selected image to use, for example ``python:3.12``.

Step 3: Resources
-----------------

.. list-table::
   :header-rows: 1
   :widths: 20 45 35

   * - Setting
     - What it controls
     - Values and default
   * - Concurrency
     - The number of executions the sandbox can run at the same time.
     - Number. Default ``1``.
   * - RAM (MB)
     - The memory available to the sandbox.
     - Number of megabytes. Default ``500``.
   * - CPU (%)
     - The share of CPU processing power available to the sandbox.
     - Percentage. Default ``20``.
   * - Security Options
     - The security profile of the container. It applies operating system level restrictions on what the container can do, separately from the User and Privileged settings.
     - Drop down. Nothing is selected by default.
   * - User
     - The account the sandbox runs as.
     - ``User`` or ``Root``. Default ``User``.
   * - Privileged
     - Whether the container receives extended capabilities.
     - ``True`` or ``False``. Default ``False``.

User values
~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Value
     - Description
   * - User
     - A standard, restricted account. It can run typical scripts and install typical packages but does not have full system level permissions.
   * - Root
     - Full administrative access inside the container.

Privileged values
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Value
     - Description
   * - False
     - The container is blocked from certain low level operations, such as accessing host hardware devices or running nested containers.
   * - True
     - The container receives extended capabilities, for example running Docker inside Docker.

Step 4: Environment
-------------------

The Environment step has one section, **Environment variables**. It stores secrets, API keys, tokens and other configuration values that the sandbox container can read. A new sandbox starts with no variables, and the step can be skipped. Variables can be added later.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Control
     - Description
   * - Add a variable
     - A button in the top right of the step. It opens a menu of ways to add a variable.
   * - Add your first variable
     - A button shown while the list is empty.

Step 5: Advanced
----------------

The Advanced step has three sections: SSH, Logs and Settings. All of them are optional.

.. list-table::
   :header-rows: 1
   :widths: 20 20 35 25

   * - Section
     - Setting
     - What it controls
     - Values and default
   * - SSH
     - SSH Enable
     - Whether direct SSH access to the sandbox is turned on.
     - Toggle. Off by default.
   * - Logs
     - Max Files
     - The number of log files the sandbox keeps before older ones are rotated out.
     - Number. Default ``2``.
   * - Logs
     - Max Size (MB)
     - The maximum size of each log file.
     - Number of megabytes. Default ``1``.
   * - Settings
     - Github connection (optional)
     - Links a GitHub repository to the sandbox so that it can pull code from the repository.
     - Drop down. Default ``None``.
   * - Settings
     - Volumes (optional)
     - Attaches persistent storage to the sandbox. A volume must already exist before it can be selected.
     - Drop down. No volume is selected by default.

Without a volume, files that the sandbox creates or changes are lost when it stops or restarts.

When all five steps are complete, click **Create Sandbox**. The new sandbox appears in the sandbox list.

Recommended defaults at a glance
--------------------------------

The following values are the product's recommended starting point for a standard Python sandbox.

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Step
     - Setting
     - Value
   * - Basic Information
     - Type and Language
     - Code and Python
   * - Image
     - Option
     - Predefined (Our Images)
   * - Resources
     - User and Privileged
     - User and False
   * - Environment
     - Variables
     - None. The step can be skipped.
   * - Advanced
     - SSH and Volumes
     - SSH off and no volume