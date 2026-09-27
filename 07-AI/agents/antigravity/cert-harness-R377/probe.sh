#!/usr/bin/env bash
# probe.sh <script> <label> [env assignments...]
S="$1"; LABEL="$2"; shift 2
cd /tmp/mf377
: > actions.log; : > state.db
out=$(env "$@" FAKE_LOG=/tmp/mf377/actions.log FAKE_STATE=/tmp/mf377/state.db \
      PATH=/tmp/mf377/bin:$PATH "$S" --execute 2>&1)
a_m=$(grep -c '^MERGE '        actions.log || true)
a_cp=$(grep -c '^CLOSE-PR '    actions.log || true)
a_rt=$(grep -c '^RETARGET '    actions.log || true)
a_ci=$(grep -c '^CLOSE-ISSUE ' actions.log || true)
rd() { printf '%s\n' "$out" | sed -n "s/.*$1 *\([0-9]*\)$/\1/p" | tail -1; }
r_m=$(rd 'PRs merged:'); r_cp=$(rd 'PRs closed:'); r_rt=$(rd 'PRs retargeted:'); r_ci=$(rd 'Issues closed:')
r_sk=$(printf '%s\n' "$out" | sed -n 's/.*gone): *\([0-9]*\)$/\1/p' | tail -1)
flag() { [ "$1" = "$2" ] && echo "  " || echo " <-LIE"; }
printf '%-46s merge %2s/%2s%s  closePR %2s/%2s%s  retgt %2s/%2s%s  closeISS %2s/%2s%s  skipped %s\n' \
  "$LABEL" "$a_m" "$r_m" "$(flag "$a_m" "$r_m")" "$a_cp" "$r_cp" "$(flag "$a_cp" "$r_cp")" \
  "$a_rt" "$r_rt" "$(flag "$a_rt" "$r_rt")" "$a_ci" "$r_ci" "$(flag "$a_ci" "$r_ci")" "$r_sk"
printf '%s\n' "$out" | grep -E '\[FAILED\]|\[HOLD\]' | sed 's/^/        /' || true
