import os
from dotenv import load_dotenv
from paradex_py.api.api_client import ParadexApiClient
from paradex_py.account.account import ParadexAccount
from paradex_py.environment import PROD

# Load environment variables from .env
load_dotenv()

# Match your actual .env file keys
eth_address = os.getenv("ETH_ADDRESS")
eth_private_key = os.getenv("ETH_PRIVATE_KEY")

if not eth_address or not eth_private_key:
    raise ValueError("Missing ETH_ADDRESS or ETH_PRIVATE_KEY in environment variables")

# Use PROD environment for mainnet
env = PROD

# Create REST client
client = ParadexApiClient(env=env, logger=None)
config = client.fetch_system_config()

# Initialize account with Ethereum credentials
account = ParadexAccount(
    config=config,
    l1_address=eth_address,
    l1_private_key=eth_private_key,
)

# Finalize account setup (generates STARK keys and headers)
client.init_account(account)

# Print out credentials and JWT headers
print("✅ JWT Authentication Successful")
print("STARKNET Address:", hex(account.l2_address))
print("STARKNET Public Key:", hex(account.l2_public_key))
print("JWT Headers:", account.auth_headers())
