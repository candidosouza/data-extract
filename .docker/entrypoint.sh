#!/bin/bash

if [ ! -f ".env" ]; then
  cp .env.example .env
fi

pip install -r requirements.txt
tail -f /dev/null
