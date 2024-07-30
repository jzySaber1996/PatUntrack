# PatUntrack

This is the repository for PatUntrack: Automated Generating Patch Examples for Issue
Reports without Tracked Insecure Code (ASE'24)

## Prompts for Insecure Code\&Patch Generation

In this section, we illustrate the initial prompt for all the subtasks in the PatUntrack.
### Pre-defined Prompt for Extracting the VTP Description $P_{extract}$


> We define the structure of the VTP description for triggering the vulnerabilities, which
is a graph with operations and transitions:
> 
> * The definition of operations and transitions in the VTP description.
> 
> Please note that each $𝑉𝑢𝑙\_𝑇𝑦𝑝𝑒$ has a CWE type and error type. Different CWE and
error types have different Focus ($f$) on extracting VTP description.
> * The definition of CWE and error types.
> * Focus List: ${⟨𝑉𝑢𝑙\_𝑇𝑦𝑝𝑒_1, 𝑓_1⟩, ..., ⟨𝑉𝑢𝑙\_𝑇𝑦𝑝𝑒_𝑛, 𝑓_𝑛⟩}$
> 
> The input IR is {Title, Body}, where Title is the summarization of vulnerability, and
Body incorporates the content of the vulnerability. Please generate the VTP description
based on the previous definition.

### Pre-defined Prompt for Completing the VTP Description $P_{complete}$


> We define the structure of the VTP description for triggering the vulnerabilities, which
is a graph with operations and transitions:
> 
> * The definition of operations and transitions in the VTP description.
> 
> Please note that each $𝑉𝑢𝑙\_𝑇𝑦𝑝𝑒$ has a CWE type and error type. Different CWE and
error types have different Focus ($f$) on extracting VTP description.
> * The definition of CWE and error types.
> * Focus List: ${⟨𝑉𝑢𝑙\_𝑇𝑦𝑝𝑒_1, 𝑓_1⟩, ..., ⟨𝑉𝑢𝑙\_𝑇𝑦𝑝𝑒_𝑛, 𝑓_𝑛⟩}$
> 
> The input VTP description is {JSON-formatted VTP Description}. 
> Please determine whether this VTP description is complete based on the previous definition.
> If the VTP description is not complete, you can generate the missing nodes and edges based on the Focus List.
> 
> The inputted IR is{Title, Body}. After you generate the complete VTP description, you can update the content of IR.
