.. _collaborator_information:


********************
collaborator_information
********************

**This module was created to manage and view collaborators of provided repositories.**


Version added: 0.0.1

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Retrieve a Github organization's provided repository. This contains collaborator information in the form of a list of dictionaries that consist of collaborators' information.
- Manage GitHub collaborators in organization repository including adding, removing, or changing collaborator permissions.


Requirements
------------
There are no further requirements needed to run this module.


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
  <!-- TOP OF TABLE -->
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th>Choices/<font color="blue">Required</font></th>
            <th width="50%">Comments</th>
        </tr>
  <!-- ACCESS_TOKEN -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>access_token</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>True</div>
                </td>
                <td>
                        <div>GitHub Token used to authenticate with the Github Rest API.</div>
                </td>
            </tr>
  <!-- ORGANIZATION -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>organization</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>True</div>
                </td>
                <td>
                        <div>Organization provided by users.</div>
                </td>
            </tr>
  <!-- API_URL -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>api_url</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <div>Unecessary in event of user token</div>
                </td>
                <td>
                        <div>False</div>
                </td>
                <td>
                        <div>An enterprise URL is necessary when a module is recieving an enterprise token. In the structure of the URL, it is vital that it includes the subdirectory path to the GitHub API as well as the correct version type. An template of this is:</div>
                        <code>https://github.&ltENTERPRISE DOMAIN&gt/api/v3</code>
                </td>
            </tr>
  <!-- REPOSITORY-->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>repository</b>                                                                            <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div></div>                                                                         <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>True</div>
                </td>
                <td>
                        <div>Repository that is part of the provided organization whose collaborators will be modified</div>  <!-- COMMENTS -->
                </td>
            </tr>
    <!-- COLLABORATOR -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>collaborator</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div>Must be a valid GitHub username</div><!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>True</div>
                </td>
                <td>
                        <div>Collaborator to be added, modified or deleted to the provided repository</div>  <!-- COMMENTS -->
                </td>
            </tr>
    <!-- PERMISSION -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>permission</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div>Default: <code>pull</code>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>The permission the collaborator will have in the repository (<code>pull</code> <code>push</code> or <code>admin</code>)</div>  <!-- COMMENTS -->
                </td>
            </tr> 
    <!-- STATE -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">str</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div>Default: <code>present</code></div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>The option to have the collaborator being <code>present</code> or <code>absent</code> in the repository.</div>  <!-- COMMENTS -->
                </td>
            </tr> 
            
       
            
            
    <!-- END OF TABLE-->      
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

   - name: "Adding/modifying collaborator in enterprise GitHub account"
     ohioit.github.collaborator_information:
       access_token: <GITHUB TOKEN>
       organization: <ORGANIZATION NAME>
       api_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
       permission: <pull, push, or admin>
       repository: <REPOSITORY NAME>
       collaborator: <VALID GITHUB USERNAME>
       state: present
       
   - name: "Delete collaborator in enterprise GitHub account"
     ohioit.github.collaborator_information:
       access_token: <GITHUB TOKEN>
       organization: <ORGANIZATION NAME>
       api_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
       repository: <REPOSITORY NAME>
       collaborator: <VALID GITHUB USERNAME>
       state: absent

Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2" width="35%">Key</th>
            <th width="15%">Returned</th>                                                                           
            <th width="50%">Description</th>
        </tr>
  <!-- COLLABORATORS -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators</b>                                                                     <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dict</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if GitHub API token connects</td>                                                                             <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Dictionary contains all repositories with the names as keys and a list of collaborator's information as the values.</div>
                </td>
            </tr>
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME> -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt]</b>                                                                     <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>List contains dicts of each collaborator's information (that are in that repository).</div>
                </td>
            </tr>
            
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME>.index -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt].&ltINDEX&gt</b>                                                        <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dict</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>This index provides access to a dictionary containing information about a single collaborator.</div>
                </td>
            </tr>
      
            
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME>.<INDEX>.id -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt].&ltINDEX&gt.id</b>                                                        <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">int</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Collaborator's id number.</div>
                </td>
            </tr>
                        
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME>.<INDEX>.login -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt].&ltINDEX&gt.login</b>                                                       <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">str</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Collaborator's login. This is their GitHub username.</div>
                </td>
            </tr>
               
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME>.<INDEX>.permissions -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt].&ltINDEX&gt.permissions</b>                                             <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dict</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Dictionary of statuses of permissions including admin, pull, push, and triage.</div>
                </td>
            </tr>
            
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME>.<INDEX>.permissions.admin -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt].&ltINDEX&gt.permissions.admin</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">bool</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Will return true if admin rights are given to collaborator. Read, clone, push, and add collaborators permissions to repository.</div>
                </td>
            </tr>
            
            
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME>.<INDEX>.permissions.push -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt].&ltINDEX&gt.permissions.push</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">bool</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Will return true if push rights are given to collaborator. Read, clone, and push to repository.</div>
                </td>
            </tr>
            
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME>.<INDEX>.permissions.pull -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt].&ltINDEX&gt.permissions.pull</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">bool</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Will return true if pull rights are given to collaborator. Read and clone repository.</div>
                </td>
            </tr>
            
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME>.<INDEX>.permissions.triage -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt].&ltINDEX&gt.permissions.triage</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">bool</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Will return true if triage rights are given to collaborator. Users with the triage role can request reviews on pull requests, mark issues and pull requests as duplicates, and add or remove milestones on issues and pull requests. No write access.</div>
                </td>
            </tr>
            
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME>.<INDEX>.site_admin -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt].&ltINDEX&gt.site_admin</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">bool</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Will return true if collaborator is a site admin. This permission gives the collaborator the ability to manage users, organizations, and repositories.</div>
                </td>
            </tr>
            
  <!-- COLLABORATORS.<ORG NAME>/<REPO NAME>.<INDEX>.type -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>collaborators[&ltORG NAME&gt/&ltREPO NAME&gt].&ltINDEX&gt.type</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">str</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one collaborator is within repository</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>This will return what type of collaborator the user is.</div>
                </td>
            </tr>
            
  <!-- CHANGED -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>changed</b>                                                                     <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">bool</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if GitHub API token connects</td>                                                                             <!-- WHEN IS IT RETURNED -->
                <td>
                            <div>Whether or not any of the collaborators were changed. This includes adding or changing permissions of collaborators. The status returned will either be true (something changed) or false (nothing changed).</div>
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
