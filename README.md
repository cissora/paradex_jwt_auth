
# Paradex JWT Auth (Python)

This repository provides a working Python implementation of Paradex JWT authentication, tested and compatible with their latest production environment.

Paradex offers robust documentation and additional community resources (which I highly recommend exploring in detail). However, developers may still encounter subtle inconsistencies or ambiguities when implementing JWT-based authentication flows — particularly around off-chain signature schemas, Pedersen hashing, and the precise structure of the authorization payloads. This repo was created to address those challenges with a working Python implementation that bridges Paradex’s SDK abstractions and its underlying cryptographic signing primitives. Through reverse-engineering message formats and normalizing .env usage across environments, I surfaced edge cases involving L1→L2 key derivation, keccak-prefixed messages, and JWT expiration handling. These insights are especially relevant for developers working across Python, Rust, or Node.js, where Paradex’s schema enforcement and onboarding logic demand exact replication of canonical byte representations. This repo provides a clean separation of signing logic, environment configuration, and REST client workflows — helping others bypass common JWT pitfalls and build production-grade integrations with confidence.

## Features

- Uses the `paradex_py` SDK
- Loads private credentials from `.env`
- Fully working JWT signature + header generation
- Minimal, no-strategy leakage
- Ready for extension to HTTP requests or WebSocket flows

## Files

| File | Purpose |
|------|---------|
| `jwt_helper_debug.py` | Core logic to fetch and print a working Paradex JWT |
| `jwt_helper.py` | Standardized JWT generator using SDK |
| `paradex_http_auth.py` | Example using JWT for HTTP request |
| `.env.example` | Example env file |
| `requirements.txt` | Python dependencies |
| `rust_jwt/` | Experimental Rust version |
| `node_jwt/` | Experimental Node.js version |

## Getting Started

```bash
git clone https://github.com/cissora/paradex_jwt_auth
cd paradex-jwt-auth-python
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Fill with your real keys
python jwt_helper_debug.py
```

## Dependencies

- `python-dotenv`
- `paradex_py`
- `requests`

## Credits

- Author: [(Twitter)](https://x.com/cissora)
- Ethereum L1 Address: `0x950BD1C17FEA646d275d1442B01d390cB3313978`
- Paradex Username: Dippy
- Paradex L2 Address: `0x3132fa8f6a3f59c6c0dd3155ceef58b3a035142e6344922979b423db137b1ac`

## License

MIT — feel free to fork, build, or contribute.
