#!/bin/bash

# Move working directory to script directory
cd "$(dirname "$0")"

# Clear up Caddy
sudo rm -rf ./caddy/config/ ./caddy/data/

# Clear up QuestDB
sudo rm -rf ./questdb/conf/ ./questdb/db/ ./questdb/public/
