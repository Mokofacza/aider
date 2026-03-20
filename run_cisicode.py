import re
from aider.main import main
from aider.coders.base_coder import Coder

original_calculate_and_show_tokens_and_cost = Coder.calculate_and_show_tokens_and_cost

def calculate_and_show_tokens_and_cost_no_cost(self, messages, completion=None):
    original_calculate_and_show_tokens_and_cost(self, messages, completion)
    if self.usage_report and " Cost: " in self.usage_report:
        self.usage_report = self.usage_report.split(" Cost: ")[0]
    if self.usage_report:
        self.usage_report = re.sub(r"\s*Cost: \$[\d\.,]+.*", "", self.usage_report)

Coder.calculate_and_show_tokens_and_cost = calculate_and_show_tokens_and_cost_no_cost

if __name__ == "__main__":
    main()
