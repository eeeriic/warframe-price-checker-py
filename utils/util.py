import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from getData.get_items import get_items
from filterData.filter_all_items import filter_all_items
from filterItems.filter_items import filter_items
from getPrices.getArcanePrices.getAllArcanePrices import getAllArcanePrices
from getPrices.getCompanionPrices.getAllCompanionSetPrices import getAllCompanionSetPrices
from getPrices.getModPrices.getAllModPrices import getAllModPrices
from getPrices.getWarframePrices.getAllWarfameSetPrices import getAllWarframeSetPrices
from getPrices.getWeaponPrices.getAllWeaponSetPrices import getAllWeaponSetPrices


def run_pipeline():
	get_items()
	filter_all_items()
	filter_items()
	getAllArcanePrices()
	getAllCompanionSetPrices()
	getAllModPrices()
	getAllWarframeSetPrices()
	getAllWeaponSetPrices()


if __name__ == "__main__":
	run_pipeline()