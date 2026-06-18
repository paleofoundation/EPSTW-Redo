#!/usr/bin/env bash
# Deploy sustainabilitydiet.com to Vercel.
# First run: prompts for browser login. Subsequent runs: just deploy.
set -e
cd "$(dirname "$0")"
npx -y vercel@latest deploy --prod --yes --name sustainabilitydiet
