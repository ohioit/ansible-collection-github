.. _repository_information:


********************
repository_information
********************

**With given user & organization, returns repository information.**


Version added: 0.0.1

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Retrieve Github organization repository information in the form of .json to further use in other modules.



Requirements
------------
There are no further requirements needed to run this module.


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="50%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>GitHub Token</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Token used to authenticate with the Github Rest API.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>org_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Organization provided by users.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    - name: "List GitHub repositories within org"
        import_role:
          name: ohioit.github.repository_info
        vars:
          github_token: "token"
          org_name: "organization_name"

Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="50%">Description</th>
        </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>Result</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">.json</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The .json data structure is composed of the repos along with their names and other useful information.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">
                          <pre><code>"repo": repo.name = {
      "owner": repo.owner.login,
      "description": repo.description,
      "private": repo.private,
      "is_template": repo.raw_data["is_template"],
      "archived": repo.archived,
      "language": repo.language,
      "visibility": repo.raw_data["visibility"],
      "url": repo.url,
      "default_branch": repo.default_branch,
      "hooks_url": repo.hooks_url,
      "clone_url": repo.clone_url
     }</code></pre>
                        </div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Brad Golski (@bgolski)
- Jacob Eicher (@jacobeicher)
- Nolan Khounborin (@khounborinn)
- Tyler Zwolenik (@TylerZwolenik)
