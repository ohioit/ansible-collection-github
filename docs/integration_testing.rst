.. _Integration_Testing:


********************
Integration Testing
********************

**These steps may be taken to complete integration testing of ansible-collection-github modules**


Version added: 0.0.1

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This article contains the necessary requirements and steps to successfully run integration tests against the ansible-collection-github modules

Requirements
------------
- Regular Github token
- Enterprise Github token
- Organization name
- Directory ``/tests/integration/vars/args.yaml`` needs to be populated with:

.. code-block:: yaml

   ---
   token: "[regular_github_token]"
   organization_name: "[regular_github_name]"
   enterprise_token: "[enterprise_github_token]"
   enterprise_organization_name: "[enterprise_organization_name]"
   enterprise_url: "[enterprise_url]"


Running Integration Tests
----------

.. note::
As of now, running the integration tests takes the same arguments needed to run the complete module
   
#. Locally running the playbook with the command ``ansible-playbook integration_test.yaml``


Status
------


Authors
~~~~~~~

- Brad Golski (@bgolski)
- Jacob Eicher (@jacobeicher)
- Nolan Khounborin (@khounborinn)
- Tyler Zwolenik (@TylerZwolenik)
