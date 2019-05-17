#!/bin/bash

echo .
echo 'Update PSUDO A...'
tbears deploy -k Keystore/test_001.json -p op0023@OP0023 -m update -o cxa196a92207cb1050262e6793c8efe37723433891 PsudoContract/psuda/psuda/
echo .
echo .
echo 'Update PSUDO B...'
tbears deploy -k Keystore/test_001.json -p op0023@OP0023 -m update -o cx92e8a4908ddd4eb6d9fd36d6d77fa3613a102892 PsudoContract/psudb/psudb/
echo .