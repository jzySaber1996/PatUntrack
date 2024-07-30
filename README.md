# PatUntrack

This is the repository for PatUntrack: Automated Generating Patch Examples for Issue
Reports without Tracked Insecure Code (ASE'24)

## Prompts for Insecure Code\&Patch Generation

In this section, we illustrate the initial prompt for all the subtasks in the PatUntrack.
### Pre-defined Prompt for Extracting the VTP Description $P_{extract}$

```
We define the structure of the VTP description for triggering the vulnerabilities, which
is a graph with operations and transitions:
* The definition of operations and transitions in the VTP description.
Please note that each 𝑉𝑢𝑙_𝑇 𝑦𝑝𝑒 has a CWE type and error type. Different CWE and
error types have different Focus (𝑓 ) on extracting VTP description.
* The definition of CWE and error types.
* Focus List: {⟨𝑉𝑢𝑙_𝑇𝑦𝑝𝑒1, 𝑓1 ⟩, ..., ⟨𝑉𝑢𝑙_𝑇 𝑦𝑝𝑒𝑛, 𝑓𝑛 ⟩}
The input IR is {Title, Body}, where Title is the summarization of vulnerability, and
Body incorporates the content of the vulnerability. Please generate the BTP description
based on the previous definition
```