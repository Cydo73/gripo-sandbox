# How to Use a Specific Python Version

GRiPO Sandbox allows you to run code inside an isolated execution environment. The Python version available to your code is determined by the **container image** used by the Sandbox.

If your application requires a specific Python version, such as Python 3.11, you can use a Docker image that contains the required Python version.

This is useful when an application depends on a particular Python release or when you need your development and production environments to use the same Python version.

## How Python Versions Are Determined

A GRiPO Sandbox runs your code using the software provided by its configured image.

For example, an image based on Python 3.11 provides the Python 3.11 interpreter.

.. note::

The Python version is determined by the Sandbox image. Specifying a Python version in your Python source code does not change the Python interpreter used to execute the program.

## Using a Python Image

The simplest way to use a specific Python version is to configure the Sandbox with a Docker image containing that version.

For example, to use Python 3.11, use:

.. code-block:: text

python:3.11-slim

You can replace `3.11` with the Python version required by your application.

## Configuring the Sandbox

To configure a Sandbox to use a specific Python version:

1. Open **GRiPOFlow**.
2. Navigate to **Sandboxes**.
3. Create a new Sandbox or open an existing Sandbox.
4. Open the Sandbox configuration.
5. Navigate to **Image Configuration**.
6. Select the option for using a custom image, if required.
7. Specify the Docker image containing the Python version you need.
8. Complete the remaining Sandbox configuration.
9. Save the Sandbox.

## Verifying the Python Version

After configuring the Sandbox, verify that the expected Python version is available.

Run:

.. code-block:: bash

python --version

For the example above, the output should be similar to:

.. code-block:: text

Python 3.11.x

You can also check the interpreter location with:

.. code-block:: bash

which python

.. tip::

Always verify the Python version from inside the Sandbox rather than assuming that the configured image was applied correctly.

## Creating a Custom Python Image

If the standard Python image does not contain all the dependencies your application needs, you can create your own Docker image based on the required Python version.

For example, the following Dockerfile creates a Python 3.11 environment with `requests` and `pandas` installed:

.. code-block:: dockerfile

FROM python:3.11-slim

RUN pip install requests pandas

WORKDIR /app

This image contains the selected Python runtime and the dependencies required by the application.

You can build the image with Docker:

.. code-block:: bash

docker build -t my-python-sandbox .

After building the image, publish it to a container registry accessible to your GRiPO Sandbox configuration.

You can then configure the Sandbox to use the published image.

## Installing Dependencies

A custom image is useful when your application requires specific Python packages.

For larger applications, you can manage dependencies using a `requirements.txt` file.

For example:

.. code-block:: text

requests
pandas
boto3

Then use:

.. code-block:: dockerfile

FROM python:3.11-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

This approach makes the environment easier to reproduce and maintain.

## Python Version and Application Compatibility

Choosing the correct Python version is important because Python packages and applications may have version-specific requirements.

For example, if an application's documentation specifies:

.. code-block:: text

Python >=3.10,<3.12

you should select a Python version that satisfies that requirement.

.. important::

Check the Python version requirements of your application and its dependencies before selecting the Sandbox image.

## Example: Python Application

Suppose you have the following Python application:

.. code-block:: python

import sys

print(f"Python version: {sys.version}")

message = "Hello from GRiPO Sandbox!"

print(message)

After configuring the Sandbox with your desired Python image, run the application and verify that the reported version matches the version required by your application.

## Troubleshooting

Python command is not found

```

If ``python`` is not available, try:

.. code-block:: bash

   python3 --version

Some Linux-based images expose the interpreter as ``python3`` rather than ``python``.

The wrong Python version is being used
```

If the Sandbox reports an unexpected Python version:

1. Check the image configured for the Sandbox.
2. Confirm that the image tag specifies the intended Python version.
3. Verify the version from inside the Sandbox.
4. Make sure you are running the intended Sandbox rather than another environment.

Dependencies fail to install

```

If a Python package fails to install, check:

* Whether the package supports your selected Python version.
* Whether the package requires system-level dependencies.
* Whether you are using a compatible version of ``pip``.
* Whether a different base image is required.

You can check the installed ``pip`` version with:

.. code-block:: bash

   python -m pip --version

Best Practices
--------------

When using specific Python versions in GRiPO Sandbox:

* Select an image that explicitly contains the required Python version.
* Pin the Python major and minor version when reproducibility is important.
* Verify the Python version from inside the Sandbox.
* Use a custom Docker image when additional dependencies or system packages are required.
* Keep application dependencies in a ``requirements.txt`` or equivalent dependency file.
* Check package compatibility before changing Python versions.
* Avoid relying on the Python version installed on your local computer.
* Use the same Python version across development, testing, and production where possible.

Summary
-------

The Python runtime in a GRiPO Sandbox is determined by the Sandbox's configured container image.

The general workflow is:

.. code-block:: text

   Choose the required Python version
              |
              v
      Select or create image
              |
              v
       Configure Sandbox
              |
              v
          Save Sandbox
              |
              v
      Run python --version
              |
              v
    Verify the expected version

For example, a Sandbox requiring Python 3.11 can use the appropriate Python 3.11-based image. For applications requiring additional dependencies, create a custom image based on the same Python version and configure the Sandbox to use it.
::
```
