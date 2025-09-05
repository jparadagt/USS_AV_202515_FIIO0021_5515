modules = ["python-3.11"]
[agent]
expertMode = true

[workflows]
runButton = "Project"

[[workflows.workflow]]
name = "Project"
mode = "parallel"
author = "agent"

[[workflows.workflow.tasks]]
task = "workflow.run"
args = "CLI App"

[[workflows.workflow.tasks]]
task = "workflow.run"
args = "Sistema Cafeteria"

[[workflows.workflow]]
name = "CLI App"
author = "agent"

[workflows.workflow.metadata]
outputType = "console"

[[workflows.workflow.tasks]]
task = "shell.exec"
args = "python src/main.py --interactivo"

[[workflows.workflow]]
name = "Sistema Cafeteria"
author = "agent"

[[workflows.workflow.tasks]]
task = "shell.exec"
args = "python main.py"

[workflows.workflow.metadata]
outputType = "console"
