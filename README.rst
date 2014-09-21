Fabric-Verbose
==============

.. image:: https://badge.fury.io/py/fabric-verbose.svg
   :target: http://badge.fury.io/py/fabric-verbose

At a glance
-----------

**fabfile.py**

.. code-block:: python

   from fabric_verbose import verbose

   # ...

   def deploy():
        with verbose("Discarding local changes") as v:
            v.run('git reset HEAD; git clean -fd; git checkout .')

        with verbose("Pulling source code") as v:
            v.run('git pull')

        with verbose("Installing requirements") as v:
            v.run('pip install -r requirements.txt')

        with verbose("Starting") as v:
            v.run('fab start')


**Output**

.. code-block::

   * Discarding local changes... Done
   * Pulling source code... Done
   * Installing requirements... Done
   * Starting... Failed

   Fatal error: /bin/sh: uwsgi: command not found

   Aborting.


Installation
------------

.. code-block:: console

   $ pip install fabric-verbose
