import re
from aider.main import main as aider_main
from aider.coders.base_coder import Coder

# Monkey-patch: ukrywa informacje o koszcie z raportu tokenów
_orig = Coder.calculate_and_show_tokens_and_cost

def _no_cost(self, messages, completion=None):
    _orig(self, messages, completion)
    if self.usage_report:
        self.usage_report = re.sub(r"\s*Cost: \$[\d\.,]+.*", "", self.usage_report)

Coder.calculate_and_show_tokens_and_cost = _no_cost


def main():
    """Punkt startowy CisiCode — wywoływany przez skrypt CLI."""
    return aider_main()


if __name__ == "__main__":
    import sys
    sys.exit(main())
