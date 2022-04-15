.. _repository_webhooks:


********************
repository_webhooks
********************

**This module was created to manage and view collaborators of provided repositories.**


Version added: 0.0.1

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Retrieve Github organization webhooks in the form of a list of dictionaries. Each dictionary then containing a single webhook's information.
- Manage GitHub webhooks in an organization's repositories including adding, removing, and editing .


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
    <!-- STATE -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>                                                             <!-- PARAMETER -->
  <!-- ORGANIZATION NAME-->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>organization_name</b>                                                                            <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>                                             <!-- TYPE -->
                    </div>
                </td>
                
                <td>
                        <div>Default: <code>present</code></div><!-- CHOICES/DEFAULTS -->
                </td>
                
                <td>
                        <div>False</div>
                </td>
                <td>
                        <div>The state can either be <code>present</code> (where the webhook will be added or modified) or <code>absent</code> (where the webhook will be deleted)</div>  <!-- COMMENTS -->
                </td>
            </tr>
    <!-- REPOSITORY -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>repository</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div></div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>True</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>The provided repository will have its webhooks modified.</div>  <!-- COMMENTS -->
                </td>
            </tr> 
    <!-- URL -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>url</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div></div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>True</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>The provided url will be the webhook that is added, deleted, or edited. This must be structured as <code>&ltSCHEME(https://)&gt&ltHOST(fakewebsite.com)&gt&ltENDPOINT(/path/end/here)&gt</code></div>  <!-- COMMENTS -->
                </td>
            </tr> 
            
    <!-- EVENTS -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>events</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div> <code>branch_protection_rule</code> <code>check_run</code> <code>check_suite</code> <code>code_scanning_alert</code> <code>commit_comment</code> <code>content_reference</code> <code>create</code> <code>delete</code> <code>deploy_key</code> <code>deployment</code> <code>deployment_status</code> <code>discussion</code> <code>discussion_comment</code> <code>fork</code> <code>github_app_authorization</code> <code>gollum</code> <code>installation</code> <code>installation_repositories</code> <code>issue_comment</code> <code>issues</code> <code>label</code> <code>marketplace_purchase</code> <code>member</code> <code>membership</code> <code>meta</code> <code>milestone</code> <code>organization</code> <code>org_block</code> <code>package</code> <code>page_build</code> <code>ping</code> <code>project_card</code> <code>project_column</code> <code>project</code> <code>public</code> <code>pull_request</code> <code>pull_request_review</code> <code>pull_request_review_comment</code> <code>push</code> <code>release</code> <code>repository_dispatch</code> <code>repository</code> <code>repository_import</code> <code>repository_vulnerability_alert</code> <code>secret_scanning_alert</code> <code>security_advisory</code> <code>sponsorship</code> <code>star</code> <code>status</code> <code>team</code> <code>team_add</code> <code>watch</code> <code>workflow_dispatch</code> <code>workflow_job</code> </div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>The list of provided events will be added to what triggers a webhook.</div>  <!-- COMMENTS -->
                </td>
            </tr> 
    <!-- CONTENT_TYPE -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>content_type</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        Default: <div><code>json</code></div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>The provided content type will be the webhook's primary content type (either <div><code>json</code> <code>form</code>).</div>  <!-- COMMENTS -->
                </td>
            </tr> 

    <!-- ADD_EVENTS -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>add_events</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div>listed in <code>events</code> </div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>When provided a list of events to add, the provided url of the webhook will recieve the additions.</div>  <!-- COMMENTS -->
                </td>
            </tr>
    <!-- REMOVE_EVENTS -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remove_events</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div>listed in <code>events</code> </div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>When provided a list of events to remove, the provided url of the webhook will remove the events.</div>  <!-- COMMENTS -->
                </td>
            </tr>
    <!-- NEW_URL -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>new_url</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div></div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>Given a url, the current webhook will be update to the new url.</div>  <!-- COMMENTS -->
                </td>
            </tr>
    <!-- NEW_CONTENT_TYPE -->
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>new_content_type</b>                                                             <!-- PARAMETER -->
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>                                             <!-- TYPE -->
                    </div>
                </td>
                <td>
                        <div></div>      <!-- CHOICES/DEFAULTS -->
                </td>
                <td>
                        <div>False</div>                                                                         <!-- REQUIRED -->
                </td>
                <td>
                        <div>Given a content type, the current webhook will be update to the new content type.</div>  <!-- COMMENTS -->
                </td>
            </tr>
    <!-- END OF TABLE-->      
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    - name: "Add/Modify webhook to GitHub repository"
      ohioit.github.repository_webhooks:
        state: present
        access_token: <GITHUB API TOKEN>
        organization: <ORGANIZATION NAME>
        api_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
        repository: "<REPOSITORY NAME>"
        url: <SCHEME("https://")><HOST("fakewebsite.com")><ENDPOINT("/path/end/here")>
        events:
          - "public"
          - "gollum"
        content_type: json

    - name: "Delete webhook in GitHub repository"
      ohioit.github.repository_webhooks:
        state: absent
        access_token: <GITHUB API TOKEN>
        organization: <ORGANIZATION NAME>
        api_url: "https://github.<ENTERPRISE DOMAIN>/api/v3"
        repository: "<REPOSITORY NAME>"
        url: <SCHEME("https://")><HOST("fakewebsite.com")><ENDPOINT("/path/end/here")>


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
  <!-- WEBHOOKS -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks</b>                                                                     <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if GitHub API token connects</td>                                                                             <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>List contains dictionaries of webhooks and their information.</div>
                </td>
            </tr>
  <!-- WEBHOOKS.<ELEMENT INDEX> -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt</b>                                                                     <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dict</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>if at least one webhook is contained within organization</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Dictionary contains keys and values of webhooks' information.</div>
                </td>
            </tr>
            
  <!-- WEBHOOKS.<ELEMENT INDEX>.ACTIVE -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.active</b>                                                        <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">bool</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook dictionary</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Status of whether the webhook is active or not.</div>
                </td>
            </tr>
      
            
  <!-- WEBHOOKS.<ELEMENT INDEX>.CONFIG -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.config</b>                                                        <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dict</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook dictionary</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>dictionary containing the webhook's content type, insecure ssl number, and the url of where to send.</div>
                </td>
            </tr>
                        
  <!-- WEBHOOKS.<ELEMENT INDEX>.CONFIG.CONTENT_TYPE -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.config.content_type</b>                                                       <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">str</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook's configuration</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>The format of the webhook being sent to the url.</div>
                </td>
            </tr>
               
  <!-- WEBHOOKS.<ELEMENT INDEX>.CONFIG.INSECURE_SSL -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.config.insecure_ssl</b>                                             <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">str</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook's configuration</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>The status of the website being sent information. Whether or not it is secure (https vs http).</div>
                </td>
            </tr>
            
  <!-- WEBHOOKS.<ELEMENT INDEX>.CONFIG.URL -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.config.url</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">str</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook's configuration</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>The url that the webhook is sending to.</div>
                </td>
            </tr>
            
            
  <!-- WEBHOOKS.<ELEMENT INDEX>.EVENTS -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.events</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook dictionary</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>List of events that trigger the webhook to send data.</div>
                </td>
            </tr>
            
  <!-- WEBHOOKS.<ELEMENT INDEX>.ID -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.id</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">int</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook dictionary</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Unique identifier for the webhook in the repository.</div>
                </td>
            </tr>
            
  <!-- WEBHOOKS.<ELEMENT INDEX>.NAME -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.name</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">str</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook dictionary</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>Name of the webhook</div>
                </td>
            </tr>
            
  <!-- WEBHOOKS.<ELEMENT INDEX>.PING_URL -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.ping_url</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">str</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook dictionary</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>The URL to ping the webhook</div>
                </td>
            </tr>
            
  <!-- WEBHOOKS.<ELEMENT INDEX>.TEST_URL -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.test_url</b>                                         <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">str</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook dictionary</td>                                                                    <!-- WHEN IS IT RETURNED -->
                <td>
                                                                                                                        <!--DESCRIPTION-->
                            <div>The url to test the webhook.</div>
                </td>
            </tr>
            
  <!-- WEBHOOKS.<ELEMENT INDEX>.URL -->
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>webhooks.&ltELEMENT INDEX&gt.test_url</b>                                                                     <!-- HOW TO ACCESS RETURNED -->
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">str</span>                                               <!-- TYPE -->
                    </div>
                </td>
                <td>provided per webhook dictionary</td>                                                                             <!-- WHEN IS IT RETURNED -->
                <td>
                            <div>The url in which the webhook resides</div>
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
