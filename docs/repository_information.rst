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
- Retrieve Github organization repository information in the form of list of dictionaries to further use in other modules.



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
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enterprise_url</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <div>Unecessary in event of user token</div>
                </td>
                <td>
                        <div>An enterprise URL is necessary when a module is recieving an enterprise token. In the structure of the URL, it is vital that it includes the subdirectory path to the GitHub API as well as the correct version type. An template of this is:</div>
                        <code>https://github.&ltENTERPRISE DOMAIN&gt/api/v3</code>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    - name: "List GitHub repositories within non-enterprise organization"
      ohioit.github.repository_information:
        token: "<TOKEN>"
        organization_name: "<ORGANIZATION NAME>"
      register: result
 
    - name: "List GitHub repositories within enterprise organization"
      ohioit.github.repository_information:
        token: "<TOKEN>"
        organization_name: "<ORGANIZATION NAME>"
        enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
      register: result
      
     

Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2" width=35%>Key</th>                  <!--KEY-->
            <th width=15%>Returned</th>                         <!--RETURNED-->
            <th width=50%">Description</th>          <!--DESCRIPTION-->
        </tr>
   <!--REPOS-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">List</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>If provided GitHub API token connects.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>List contains dictionaries of repositories and their information.</div>
                </td>
            </tr>
   <!--REPOS.ELEMENT INDEX-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Dict</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo is contained within organization.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>Dictionary contains keys and values of a repository's information.</div>
                </td>
            </tr>
    <!--REPOS.ELEMENT INDEX.NAME-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.name</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Str</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>Repository's name.</div>
                </td>
            </tr>
   <!--REPOS.ELEMENT INDEX.FULL_NAME-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.full_name</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Str</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>Repository path name starting from organization.</div>
                </td>
            </tr>
   <!--REPOS.ELEMENT INDEX.OWNER-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.owner</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Str</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>Name of organization that owns the repository.</div>
                </td>
            </tr>
   <!--REPOS.ELEMENT INDEX.DESCRIPTION-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.<br>description</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Str</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>Description of the repository. This field will be null unless previously set.</div>
                </td>
            </tr>
            
   <!--REPOS.ELEMENT INDEX.PRIVATE-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.private</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Bool</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>Status whether the repository is private (true) or public (false).</div>
                </td>
            </tr>
            
   <!--REPOS.ELEMENT INDEX.ARCHIVED-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.archived</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Bool</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>Status whether the repository is archived or not.</div>
                </td>
            </tr>
   <!--REPOS.ELEMENT INDEX.LANGUAGE-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.language</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Str</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>Repository language. This can be any language listed <a href="https://github.com/github/linguist/blob/master/lib/linguist/languages.yml">here</a>.</div>
                </td>
            </tr>            
   <!--REPOS.ELEMENT INDEX.URL-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.url</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Str</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>URL for repository. The provided URL is the route used for the GitHub API to be connected to Ansible. Non-enterprise URLs will be structured as <br><code>https://api.github.com/repos/&ltORGANIZATION NAME&gt/&ltREPO NAME&gt</code>.<br>Enterprise URLs are structured as <br><code>https://github.&ltENTERPRISE DOMAIN&gt/api/v3/repos/&ltORGANIZATION NAME&gt/&ltREPO NAME&gt</code>.</div>
                </td>
            </tr>            
   <!--REPOS.ELEMENT INDEX.DEFAULT_BRANCH-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.default_branch</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Str</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>The branch that GitHub displays when anyone visits your repository.</div>
                </td>
            </tr>            
            
   <!--REPOS.ELEMENT INDEX.HOOKS_URL-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.hooks_url</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Str</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>URL location where hooks are located within the repository when connected to the GitHub API. Non-enterprise URLs will be structured as <br><code>https://api.github.com/repos/&ltORGANIZATION NAME&gt/&ltREPO NAME&gt/hooks</code>.<br>Enterprise URLs are structured as <br><code>https://github.&ltENTERPRISE DOMAIN&gt/api/v3/repos/&ltORGANIZATION NAME&gt/&ltREPO NAME&gt/hooks</code>.</div>
                </td>
            </tr>         
            
            
            
   <!--REPOS.ELEMENT INDEX.CLONE_URL-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.clone_url</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Str</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>URL location where repository will be accessible to be cloned. Non-enterprise URLs will be structured as <br><code>https://github.com/&ltORGANIZATION NAME&gt/&ltREPO NAME&gt.git</code>.<br>Enterprise URLs are structured as <br><code>https://github.&ltENTERPRISE DOMAIN&gt/&ltORGANIZATION NAME&gt/&ltREPO NAME&gt.git</code>.</div>
                </td>
            </tr>  
   <!--REPOS.ELEMENT INDEX.VISIBILITY-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.visibility</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Str</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified and organization is NOT part of an enterprise account.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>The repository visibility status will be 'public', 'internal', or 'private'.</div>
                </td>
            </tr>    
   <!--REPOS.ELEMENT INDEX.IS_TEMPLATE-->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>repos.&ltELEMENT INDEX&gt.is_template</b>                                                                     <!--KEY-->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">Bool</span>                                               <!--TYPE-->
                    </div>
                </td>
                <td>Only if at least one repo has been identified and organization is NOT part of an enterprise account.</td>                                                                             <!--RETURNED-->
                <td>         <!--DESCRIPTION-->
                            <div>The repository template status will true or false. </div>
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
