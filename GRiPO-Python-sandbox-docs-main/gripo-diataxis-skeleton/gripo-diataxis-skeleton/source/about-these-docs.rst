How these docs are organised
============================

.. Delete this comment when the page is finished. This page shows that the
   structure was a deliberate choice. Keep it short and honest. Update the
   mapping table to match what you actually moved.

These docs follow the Diátaxis framework. It separates documentation into four kinds of page, because a reader who wants to learn needs something different from a reader who wants to finish a task or look up a fact.

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Kind of page
     - The reader wants to
     - Where to find it
   * - Tutorial
     - Learn by doing
     - :doc:`tutorials/create-your-first-python-sandbox`
   * - How to guide
     - Finish a specific task
     - :doc:`howto/use-a-specific-python-version`, :doc:`howto/add-an-environment-variable`
   * - Reference
     - Look up a fact
     - :doc:`reference/sandbox-settings`
   * - Explanation
     - Understand why
     - :doc:`explanation/sandbox-security-and-isolation`

What changed
------------

[Two or three sentences in your own words: the original Python guide tried to teach, instruct, define and explain on one page. Say what problem that caused for readers.]

Where each part of the original guide went
------------------------------------------

This is a draft mapping. Edit it to match what you moved.

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - In the original Python guide
     - Now lives in
   * - The recommended path through the wizard
     - Tutorial
   * - Field by field definitions and the sandbox list columns
     - Reference
   * - "What happens if you get this wrong" passages, Root versus User, Privileged, image trust, storage
     - Explanation
   * - Using a specific Python version, adding an API key
     - How to guides
   * - Quick Recap table
     - Reference, under "Recommended defaults at a glance"

The original guides are still available under :doc:`create-python-sandbox` for comparison.
