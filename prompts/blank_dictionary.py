BLANK_DICTIONARY= '''You are an intelligent agent with excellent ability to comprehend
English language. Your task is to take a dictionary and convert it into a blank dictionary
which means the dictionary should have the same structure and the same keys 
but the values should be empty strings.

Example:
claim_dict = {
    "claim": "The sky is blue",
    "evidence": "The sky appears blue due to the scattering of light",
    "source": "NASA"
}
blank_dict = {
    "claim": "",
    "evidence": "",
    "source": ""
}
The response should be only the dictionary and nothing else.
**BE VERY CAREFUL WHEN ANALYZING THE DICTIONARY AS IT'S VERY IMPORTANT TO 
STRUCTURE THE DICTIONARY ACCURATELY**'''