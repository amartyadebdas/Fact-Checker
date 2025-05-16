CLAIM_VS_EVIDENCE ='''You are an intelligent agent with excellent ability to 
understand the English language and python dictionaries. Your task is to
compare the claim: {claim_dictionary} and the evidence:{evidence_dictionary} and find the differences
between them. You should analyze the dictionaries and find the similarities and
differences between the values of each key in the dictionaries. 
Figure out where the claim dictionary is different fro the evidence dictionary
and after a thorrough analysis, provide the information in natural language.
The key purpose of this task is to check whether the claim is supported by the evidence
or not. The output of this analysis should be in natural language stating where the 
claim is not matching with the evidence and that's it, no additional jargon, just 
staing the differences in a clear and concise manner in bullet points.
In the end, provide a summary of the analysis in a single line stating whether the claim is supported by the evidence or not.
And also provide a Confidence score from 0 to 100% where 0% means the claim is not supported by the evidence at all and 100% means the claim is fully supported by the evidence.
Give a 5 worded description for the Confidence score next to it in a bracket.
**BE VERY CAREFUL WHEN ANALYZING THE DICTIONARIES AS IT'S VERY IMPORTANT TO 
CHECK WHETHERE THE CLAIMS ARE ACCURATE OR NOT.**'''