.. _Unit_Testing:


********************
Unit Testing
********************

**These steps may be taken to complete unit testing of ansible-collection-github modules**


Version added: 0.0.1

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This article contains the necessary requirements and steps to successfully run unit tests against the ansible-collection-github modules



Requirements
------------
- A virtual development environment (venv or docker)
- Tests need to be ran with Python3

Setting Up Virtual Environment
----------

#. Clone the ansible repository: ``$ git clone https://github.com/ansible/ansible.git``
#. Change your working directory: ``$ cd ansible``
#. Virtual environment package should be downloaded: ``$ pip install virtualenv``
#. Virtual environment needs to be created: ``$ python3 -m venv venv``
#. Virtual environment needs to be activated: ``$ . venv/bin/activate``
#. Requirements need to be installed: ``$ pip install -r requirements.txt``
#. To obtain requirements for unit testing: ``$ pip install -r /test/units/requirements.txt``
#. The environment seteup script for each new dev shell: ``$ . hacking/env-setup``

*If virtual environement has already been created, within* ``ansible`` *, run command* ``$ . venv/bin/activate && . hacking/env-setup``

Running Unit Tests
----------

#. Set up and start virtual environment (run ``$ . venv/bin/activate && . hacking/env-setup`` if virtual environment has been created previously)
#. Locate and change to the ``ansible-collection-github`` directory
#. Run the command ``ansible-test units --python 3.[YOUR PYTHON VERSION] --venv`` to run tests.





Status
------


Authors
~~~~~~~

- Brad Golski (@bgolski)
- Jacob Eicher (@jacobeicher)
- Nolan Khounborin (@khounborinn)
- Tyler Zwolenik (@TylerZwolenik)
