each agent/subagent will manage their own folder in scratchpad/
the naming convention for folders is the <agent name>_scratch

An agent/subagent can draft:
1. <topic>_findings_<version_number>.md which comprises findings from it's delegated scope ONLY
2. to_<agent name>_<topic>_<version_number>.md which are messages to other agents/subagents

if a message markdown happens to be addressed to multiple subagents, then delimit by `-` hyphens. For example:
to_X-Y_animalfact_1.md