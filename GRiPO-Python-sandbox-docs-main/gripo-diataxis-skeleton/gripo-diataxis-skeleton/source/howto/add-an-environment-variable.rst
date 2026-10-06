# How to Add an Environment Variable

Environment variables allow you to provide configuration values to code running inside a GRiPO Sandbox without hard-coding those values directly into your application.

They are commonly used for configuration such as API endpoints, application modes, feature flags, and other values that may change between environments.

For sensitive values such as API keys, passwords, and access tokens, use GRiPO's credential and secret-management features where available rather than storing secrets directly in your code.

## Prerequisites

Before adding an environment variable, make sure you have:

* Access to a GRiPO account.
* A GRiPO Sandbox.
* Permission to configure the Sandbox.
* A script or application that will read the environment variable.

## Adding an Environment Variable

To add an environment variable to a Sandbox:

1. Open **GRiPOFlow**.
2. Navigate to **Sandboxes**.
3. Open the Sandbox you want to configure, or create a new Sandbox.
4. Open the Sandbox's configuration/settings.
5. Locate the **Environment Variables** section.
6. Add a new environment variable.
7. Enter the variable's **name** and **value**.
8. Save the Sandbox configuration.

For example, you can create the following environment variable:

.. code-block:: text

API_URL=https://api.example.com

The variable name is `API_URL` and its value is `https://api.example.com`.

.. note::

Environment variable names are conventionally written using uppercase letters with underscores separating words. For example, use `API_URL` rather than `api url`.

## Using an Environment Variable in Python

Once the environment variable has been added to the Sandbox, your Python code can access it through Python's built-in :mod:`os` module.

For example:

.. code-block:: python

import os

api_url = os.getenv("API_URL")

print(api_url)

If `API_URL` has been configured as:

.. code-block:: text

https://api.example.com

the Python program will retrieve that value when it runs inside the Sandbox.

## Checking Whether a Variable Exists

You can check whether an environment variable has been configured before using it:

.. code-block:: python

import os

api_url = os.getenv("API_URL")

if api_url:
print("API_URL is configured")
else:
print("API_URL is not configured")

## Providing a Default Value

You can provide a default value when an environment variable is not set.

.. code-block:: python

import os

environment = os.getenv("ENVIRONMENT", "development")

print(environment)

If `ENVIRONMENT` exists, its configured value is returned. If it does not exist, Python uses `development` instead.

## Using a Required Environment Variable

For values that your application cannot run without, you may want the program to stop with a clear error message if the variable is missing.

.. code-block:: python

import os

api_key = os.environ.get("API_KEY")

if not api_key:
raise RuntimeError("API_KEY environment variable is not configured")

print("API key is configured")

This approach makes configuration problems easier to identify during Sandbox execution.

## Verifying an Environment Variable

You can verify that a variable is available inside the Sandbox by printing a non-sensitive value:

.. code-block:: python

import os

print(os.getenv("ENVIRONMENT"))

For example, if the Sandbox contains:

.. code-block:: text

ENVIRONMENT=production

the output should be:

.. code-block:: text

production

.. warning::

Do not print passwords, API keys, access tokens, or other sensitive environment variables to Sandbox logs. Logs may be visible to users or retained as part of an execution record.

## Environment Variables and Secrets

Environment variables are useful for separating application configuration from application code. However, an environment variable itself is not automatically a secure secret store.

For example, avoid hard-coding an API key directly into your Python code:

.. code-block:: python

api_key = "your-api-key"

Instead, configure the value through GRiPO's supported secret or credential-management functionality and retrieve it from the environment at runtime:

.. code-block:: python

import os

api_key = os.getenv("API_KEY")

This keeps sensitive configuration out of your source code.

.. important::

Never commit API keys, passwords, database credentials, or access tokens to your source-control repository.

## Example: Using an API Configuration

The following example demonstrates how environment variables can be used to configure a Python application.

First, configure the Sandbox with:

.. code-block:: text

API_URL=https://api.example.com
ENVIRONMENT=production

Then use the variables in your Python application:

.. code-block:: python

import os

api_url = os.getenv("API_URL")
environment = os.getenv("ENVIRONMENT", "development")

print(f"API URL: {api_url}")
print(f"Environment: {environment}")

This allows the same Python code to run in different environments without changing the source code.

For example, you could use:

.. code-block:: text

ENVIRONMENT=development

in one Sandbox and:

.. code-block:: text

ENVIRONMENT=production

in another.

The application code remains unchanged.

## Troubleshooting

Environment variable is not available

```

If your application cannot find an environment variable:

* Check that the variable name is spelled correctly.
* Check that the variable was added to the correct Sandbox.
* Make sure the Sandbox configuration was saved.
* Verify that your code uses the exact same variable name.
* Restart or create a new execution after changing the Sandbox configuration if necessary.

For example, these names are different:

.. code-block:: text

   API_URL
   api_url
   Api_Url

Environment variable contains an unexpected value
```

Check the value configured in the Sandbox and make sure it does not contain unintended spaces or characters.

You can temporarily inspect a non-sensitive configuration value with:

.. code-block:: python

import os

print(repr(os.getenv("ENVIRONMENT")))

Using `repr()` can make leading or trailing whitespace easier to identify.

## Best Practices

When working with environment variables in GRiPO Sandbox:

* Use descriptive variable names such as `API_URL` or `DATABASE_HOST`.
* Use uppercase names with underscores for consistency.
* Keep configuration separate from application code.
* Do not hard-code secrets in source code.
* Do not commit secrets to Git repositories.
* Avoid printing sensitive values to execution logs.
* Use default values only where a sensible default exists.
* Validate required configuration when the application starts.
* Use GRiPO's supported credential or secret-management functionality for sensitive values.

## Summary

Environment variables provide a convenient way to configure applications running inside a GRiPO Sandbox.

The general workflow is:

.. code-block:: text

Add variable to Sandbox
|
v
Save Sandbox configuration
|
v
Run your application
|
v
Read variable from the environment
|
v
Use the value in your code

For Python applications, environment variables can be accessed using `os.getenv()` or `os.environ`.

For example:

.. code-block:: python

import os

value = os.getenv("MY_VARIABLE")

This approach allows you to change configuration without modifying your application code.
