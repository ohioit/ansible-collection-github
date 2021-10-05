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


Running Integration Tests
----------
- As of now, running the integration tests takes the same arguements needed to run the complete module
#. Filling out the required fields of the playbook in ``/tests/integration/integration_test.yaml``
#. Locally running the playbook with the command ``ansible-playbook integration_test.yaml``





Status
------


Authors
~~~~~~~

- Brad Golski (@bgolski)
- Jacob Eicher (@jacobeicher)
- Nolan Khounborin (@khounborinn)
- Tyler Zwolenik (@TylerZwolenik)
