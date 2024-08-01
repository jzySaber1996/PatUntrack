# PatUntrack

This is the repository for PatUntrack: Automated Generating Patch Examples for Issue
Reports without Tracked Insecure Code (ASE'24)

## Abstract

Security patches are essential for enhancing the stability and robustness of projects in the open-source software community. 
While vulnerabilities are officially expected to be patched before being disclosed, patching vulnerabilities is complicated and remains a struggle for many organizations. 
To patch vulnerabilities, security practitioners typically track vulnerable issue reports (IRs), and analyze their relevant insecure code to generate potential patches. 
However, the relevant insecure code may not be explicitly specified and practitioners cannot track the insecure code in the repositories, thus limiting their ability to generate patches. 
In such cases, providing examples of insecure code and the corresponding patches would benefit the security developers to better locate and resolve the actual insecure code. 
In this paper, we propose PatUntrack, an automated approach to generating patch examples from IRs without tracked insecure code. PatUntrack utilizes auto-prompting to optimize the Large Language Model (LLM) to make it applicable for analyzing the vulnerabilities described in IRs and generating appropriate patch examples. 
To evaluate the performance of PatUntrack, we conducted experiments on 5,465 vulnerable IRs. The experimental results show that PatUntrack can obtain the highest performance and improve the traditional LLM baselines by +17.7% (MatchFix) and +14.6% (Fix@10) on average in patch example generation. 
Our human evaluation indicates that developers can benefit from these examples for patching the vulnerabilities.

## Prompts of PatUntrack
The prompts in the PatUntrack control the generation of insecure code and patch examples from the IRs.
Note that, the focus list is the essential information, and we will maintain a directory in the [prompt/focus_list](./prompt/focus_list) that store all the information in the focuses of prompt.
All the tasks will refer to the focus list to enhance their performances.

### Prompts for Generating Complete VTP Description

In this section, we illustrate the initial prompt for generating VTP descriptions in the PatUntrack.

**P_extract: Pre-defined Prompt for Extracting the VTP Description**


> We define the structure of the VTP description for triggering the vulnerabilities, which
is a graph with operations and transitions:
> 
> * The definition of operations and transitions in the VTP description.
> 
> Please note that each Vul_Type has a CWE type and error type. Different CWE and
error types have different Focus (f) on extracting VTP description.
> * The definition of CWE and error types.
> * Focus List: <Vul_Type_1,f_1>,...,<Vul_Type_n,f_n>
> 
> The input IR is {Title, Body}, where Title is the summarization of vulnerability, and
Body incorporates the content of the vulnerability. Please generate the VTP description
based on the previous definition. 
> 
> You can first predict the vulnerability types based on the CWE and error types, 
> then refer to the Focus List to retrieve the f_i for help.

**P_complete: Pre-defined Prompt for Completing the VTP Description**


> We define the structure of the VTP description for triggering the vulnerabilities, which
is a graph with operations and transitions:
> 
> * The definition of operations and transitions in the VTP description.
> 
> Please note that each Vul_Type has a CWE type and error type. Different CWE and
error types have different Focus (f) on extracting VTP description.
> * The definition of CWE and error types.
> * Focus List: <Vul_Type_1,f_1>,...,<Vul_Type_n,f_n>
> 
> The input VTP description is {JSON-formatted VTP Description}. 
> Please determine whether this VTP description is complete based on the previous definition.
> If the VTP description is not complete, you can generate the missing nodes and edges based on the Focus List.
> 
> The inputted IR is{Title, Body}. After you generate the complete VTP description, you can update the content of IR.
> 
> Based on the predicted vulnerability type {CWE and Vul_Type}, 
> you can refer to the Focus List to retrieve the f_i for help.

### Prompts for Correcting Hallucinatory VTP Description

In this section, we illustrate the initial prompt for correcting hallucinatory VTP descriptions in the PatUntrack.
The control of the traversing is in the algorithm. 
For each _OpItem_, we find it connected nodes _OpConn_ and the historical paths.
The path is _HistoricalPath: (Op_1,...,OpItem)_

**P_halDetect: Pre-defined Prompt for Detecting the LLM Hallucination**

> We define the structure of the VTP description for triggering the vulnerabilities, which
is a graph with operations and transitions:
> 
> * The definition of operations and transitions in the VTP description.
> 
> Please note that each Vul_Type has a CWE type and error type. Different CWE and
error types have different Focus (f) on extracting VTP description.
> * The definition of CWE and error types.
> * Focus List: <Vul_Type_1,f_1>,...,<Vul_Type_n,f_n>
> 
> The current node of VTP Description is shown as follows, and this VTP is completed. 
> * Current operation node: {Content of _OpItem_}.
> * The connected operation nodes: {Contents of All _OpConn_}.
> * The historical information of transitions: {JSON-formatted _HistoricalPath_}
> 
> In this task, please correct the hallucinatory in the VTP description with the following two steps.
> 
> STEP-1: You only need to generate the MySQL queries, and wait for the response. 
> The query items are golden knowledge, and we give some examples for the query.
> * Provide some SQL query examples for the golden knowledge retrieval, 
> such as "select * from DB where DB.detail like 'XSS attacks'".
> 
> STEP-2: Based on the current operation node, connected operation nodes, and historical information,
> please compare them with the {Golden Knowledge}, and report whether this node contains the hallucination.
> You just need to tell me which node and edge may contain hallucinations in JSON format.
> * Provide an example list of nodes/edges of hallucination, 
> such as {Nodes: [_OpItem_,_OpConn_1_,_OpConn_3_], Edges: [_OpItem_->_OpConn_1_,_OpItem_->_OpConn_3_]}.
> 
> Based on the predicted vulnerability type {CWE and Vul_Type}, 
> you can refer to the Focus List to retrieve the f_i for help.


Note that, in this prompt, we utilize one prompt to incorporate the two steps: query generation and hallucination detection.
In practical usage, these prompt may separately conduct these two steps.
When we receive the golden knowledge of STEP-1, we will use it in the STEP-2.

**P_halCorrect: Pre-defined Prompt for Correcting the LLM Hallucination**

> We define the structure of the VTP description for triggering the vulnerabilities, which
is a graph with operations and transitions:
> 
> * The definition of operations and transitions in the VTP description.
> 
> Please note that each Vul_Type has a CWE type and error type. Different CWE and
error types have different Focus (f) on extracting VTP description.
> * The definition of CWE and error types.
> * Focus List: <Vul_Type_1,f_1>,...,<Vul_Type_n,f_n>
> 
> The input is the {Original Nodes and Edges}, {Hallucinatory Nodes and Edges} that may contain the LLM hallucination, 
> together with the {Golden Knowledge}.
> You should tell me how to correct the hallucination, and just output the nodes and edges after you correct.
> The output will be the JSON format, and incorporates a field with description of why you correct it into this output.
> 
> * Provide an example outputted nodes and edges after hallucination correction.
> 
> Based on the predicted vulnerability type {CWE and Vul_Type}, 
> you can refer to the Focus List to retrieve the f_i for help.

### Prompts for Generating Insecure Code & Patch Example

In this section, we illustrate the initial prompt for generating insecure code & patch examples.


**P_typePredict: Pre-defined Prompt for Predicting Patch Types**

> We define the structure of the VTP description for triggering the vulnerabilities, which
is a graph with operations and transitions:
> 
> * The definition of operations and transitions in the VTP description.
> 
> Please note that each Vul_Type has a CWE type and error type. Different CWE and
error types have different Focus (f) on extracting VTP description.
> * The definition of CWE and error types.
> * Focus List: <Vul_Type_1,f_1>,...,<Vul_Type_n,f_n>
>
> The input is the {JSON-Formatted VTP Description with Corrected LLM Hallucinations}.
> Please predict which patch type of this VTP description will be used.
> * The definition of patch types <Pat_Type_1,...,Pat_Type_n>
> 
> Based on the predicted vulnerability type {CWE and Vul_Type}, 
> you can refer to the Focus List to retrieve the f_i for help.

Note that, the information in focus list f_i will incorporate the historical frequency of vulnerability types to the patch type.
This is controlled by our code and algorithm.

**P_generate: Pre-defined Prompt for Jointly Generating Insecure Code & Patch Examples**

> We define the structure of the VTP description for triggering the vulnerabilities, which
is a graph with operations and transitions:
> 
> * The definition of operations and transitions in the VTP description.
> 
> Please note that each Vul_Type has a CWE type and error type. Different CWE and
error types have different Focus (f) on extracting VTP description.
> * The definition of CWE and error types.
> * Focus List: <Vul_Type_1,f_1>,...,<Vul_Type_n,f_n>
>
> The input is the {JSON-Formatted VTP Description with Corrected LLM Hallucinations},
> and the predicted patch types is {Patch Type}.
> Please generate {K} the potential insecure code and security patch example based on these inputs.
> The format of output will be the JSON-based lists for the code pairs as follows:
> * Provide examples for the generated code pairs, such as
> {CodePair_1: {InsCode: 'InsCodeDetail', PatCode: 'PatCodeDetail'},...,CodePair_K: {InsCode: 'InsCodeDetail', PatCode: 'PatCodeDetail'}}
> 
> Based on the predicted vulnerability type {CWE and Vul_Type}, 
> you can refer to the Focus List to retrieve the f_i for help.