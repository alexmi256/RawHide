#!/usr/bin/env bash
# Generate random payload files for upload/encode testing.
#
# Usage:
#   tools/make_test_payloads.sh [COUNT] START_MB MAX_MB STEP_MB
#
# COUNT defaults to 1 and is the number of files per size. Sizes are in
# MiB (1 MB = 1024 * 1024 bytes). Files land in $OUT_DIR (default:
# ./test-payloads) as payload_<size>mb_<n>.bin.
#
# Examples:
#   tools/make_test_payloads.sh 10 30 10            # 10, 20, 30 MB
#   OUT_DIR=payloads tools/make_test_payloads.sh 5 50 150 10
#       # five files each at 50, 60, ..., 150 MB
set -euo pipefail

usage() {
    sed -n '2,14p' "$0" | sed 's/^# \{0,1\}//'
}

case $# in
    3)
        count=1
        start_mb=$1
        max_mb=$2
        step_mb=$3
        ;;
    4)
        count=$1
        start_mb=$2
        max_mb=$3
        step_mb=$4
        ;;
    *)
        usage >&2
        exit 2
        ;;
esac

for name in count start_mb max_mb step_mb; do
    if [[ ! ${!name} =~ ^[0-9]+$ ]]; then
        echo "error: $name must be a non-negative integer (got ${!name})" >&2
        exit 2
    fi
done

if (( count < 1 )); then
    echo "error: count must be at least 1" >&2
    exit 2
fi
if (( start_mb < 1 )); then
    echo "error: starting size must be at least 1 MB" >&2
    exit 2
fi
if (( step_mb < 1 )); then
    echo "error: increment must be at least 1 MB" >&2
    exit 2
fi
if (( max_mb < start_mb )); then
    echo "error: max size ($max_mb MB) is below the starting size ($start_mb MB)" >&2
    exit 2
fi

out_dir=${OUT_DIR:-test-payloads}
mkdir -p "$out_dir"

for ((mb = start_mb; mb <= max_mb; mb += step_mb)); do
    for ((n = 1; n <= count; n++)); do
        file=$(printf '%s/payload_%03dmb_%02d.bin' "$out_dir" "$mb" "$n")
        dd if=/dev/urandom of="$file" bs=1M count="$mb" status=none
        printf '%s\n' "$file"
    done
done
