


import os
from pathlib import Path
from ceres.cmds.init_funcs import chia_init
# from ceres.util.config import get_all_coin_names


# def init_all():
#     coins_names = get_all_coin_names()

#     for coin in coins_names:
#         root_path = Path(os.path.expanduser(os.getenv(f"{coin.upper()}_ROOT", f"~/.{coin}/mainnet"))).resolve()
#         # chia_init(coin, root_path)
#         chia_init(root_path, coin)