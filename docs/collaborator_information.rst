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
- Retrieve Github organization collaborator information in the form of a dictionary of repositories. Each dictionary then containing a list of dictionaries that consist of collaborators' information.
- Manage GitHub collaborators in organization repositories including adding, removing, or changing collaborator permissions.


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
  <!-- GITHUB TOKEN -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>token</b>
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
  <!-- ORG_NAME -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>organization_name</b>
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
  <!-- ENTERPRISE_URL -->
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
                        <div>False</div>
                </td>
                <td>
                        <div>An enterprise URL is necessary when a module is recieving an enterprise token. In the structure of the URL, it is vital that it includes the subdirectory path to the GitHub API as well as the correct version type. An template of this is:</div>
                        <code>https://github.&ltENTERPRISE DOMAIN&gt/api/v3</code>
                </td>
            </tr>
  <!-- REPOSITORIES LIST-->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>repos</b>                                                                            <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div></div>                                                                         <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>True</div>
                </td>
                <td>
                        <div>List of repositories is provided by user to perform further action upon their collaborators.</div>  <!-- COMMENTS -->
                </td>
            </tr>
    <!-- COLLABORATORS TO ADD-->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>collaborators_to_add</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list/dict</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div>Add by providing a list of dicts of collaborators to add along with their permissions or provide a single collaborator with their intended permission</div><!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>
                </td>
                <td>
                        <div>Collaborator(s) are added along with their intended permissions (Read, Triage, Write, or Admin) to the provided list of repos</div>  <!-- COMMENTS -->
                </td>
            </tr>
    <!-- COLLABORATORS TO REMOVE -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>collaborators_to_remove</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list of string</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div>Delete collaborator(s) by providing a list of collaborator names (as strings).</div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>This will delete all of the provided collaborators from the given repositories.</div>  <!-- COMMENTS -->
                </td>
            </tr> 
    <!-- CHECK COLLABORATOR -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>check_collaborator</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dict</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div>A name as the Key and a permission to check is provided by the user.</div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>This will check the provided permission against the given repos.</div>  <!-- COMMENTS -->
                </td>
            </tr> 
            
    <!-- COLLABORATORS TO CHANGE -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>collaborators_to_change</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dict</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div>A name as the Key and a permission to check is provided by the user.</div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>This will check the provided permission against the given repos.</div>  <!-- COMMENTS -->
                </td>
            </tr> 
       
            
            
    <!-- END OF TABLE-->      
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    - name: "Listing collaborators from enterprise GitHub account"
      ohioit.github.collaborator_information:
        token: "<GITHUB TOKEN>"
        organization_name: "<ORGANIZATION NAME>"
        enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
        repos:
          - "<REPO 1>"
          - "<REPO 2>"
          - "<REPO 3>"
      register: result

    - name: "Adding collaborators from enterprise GitHub account"
      ohioit.github.collaborator_information:
        token: "<GITHUB TOKEN>"
        organization_name: "<ORGANIZATION NAME>"
        enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
        repos:
          - "<REPO 1>"
          - "<REPO 2>"
          - "<REPO 3>"
        collaborators_to_add:
          <GITHUB USERNAME>: "<triage, pull, push or admin>"
          <ANOTHER GITHUB USERNAME>: "<triage, pull, push or admin>"
          
      register: result

    - name: "Check permissions of collaborators from enterprise GitHub account"
      ohioit.github.collaborator_information:
        token: "<GITHUB TOKEN>"
        organization_name: "<ORGANIZATION NAME>"
        enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
        repos:
          - "<REPO 1>"
          - "<REPO 2>"
          - "<REPO 3>"
        check_collaborator:
          <GITHUB USERNAME>: "<triage, pull, push or admin>"
          <ANOTHER GITHUB USERNAME>: "<triage, pull, push or admin>"

      register: result

    - name: "Change permissions of collaborators from enterprise GitHub account"
      ohioit.github.collaborator_information:
        token: "<GITHUB TOKEN>"
        organization_name: "<ORGANIZATION NAME>"
        enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
        repos:
          - "<REPO 1>"
          - "<REPO 2>"
          - "<REPO 3>"
        collaborators_to_change:
          <GITHUB USERNAME>: "<triage, pull, push or admin>"
          <ANOTHER GITHUB USERNAME>: "<triage, pull, push or admin>"
      register: result

    - name: "Remove permissions of collaborators from enterprise GitHub account"
      ohioit.github.collaborator_information:
        token: "<GITHUB TOKEN>"
        organization_name: "<ORGANIZATION NAME>"
        enterprise_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
        repos:
          - "<REPO 1>"
          - "<REPO 2>"
          - "<REPO 3>"
        collaborators_to_remove:
          - "<GitHub Username>"
          - "<GitHub Username>"
      register: result
      
     

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
