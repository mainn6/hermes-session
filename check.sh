#!/bin/bash
# Hermes 세션 완료 체크 — 참가자용. 비밀값은 출력하지 않는다.
# ponytail: config.yaml/.env를 grep으로 읽는다. yaml 라이브러리·hermes config get 없는 구버전도 통과하게.
H="${HERMES_HOME:-$HOME/.hermes}"; CFG="$H/config.yaml"; ENVF="$H/.env"
pass(){ printf "  PASS  %s\n" "$1"; }
fail(){ printf "  FAIL  %s\n      -> %s\n" "$1" "$2"; }
echo "== Hermes 세션 체크 =="
if command -v hermes >/dev/null 2>&1; then pass "hermes 설치됨 ($(hermes --version 2>/dev/null | head -1 | cut -c1-40))"; else fail "hermes 명령 없음" "터미널을 새로 열거나 source ~/.zshrc 후 다시. 없으면 STEP 01"; exit 1; fi
# model: 블록에서 값 뽑기 (첫 model: 이후 들여쓴 줄만)
blk=$(awk '/^model:/{f=1;next} f&&/^[^ ]/{f=0} f' "$CFG" 2>/dev/null)
prov=$(echo "$blk" | awk -F': *' '/^ *provider:/{print $2}' | tr -d ' "'"'")
url=$(echo "$blk"  | awk -F': *' '/^ *base_url:/{print $2}' | tr -d ' "'"'")
mdl=$(echo "$blk"  | awk -F': *' '/^ *default:/{print $2}' | tr -d ' "'"'")
key=$(echo "$blk"  | awk -F': *' '/^ *api_key:/{print $2}' | tr -d ' "'"'")
[ -z "$key" ] && key=$(grep -E '^(DGRID_API_KEY|OPENAI_API_KEY)=' "$ENVF" 2>/dev/null | head -1 | cut -d= -f2- | tr -d '"'"'")
if [ "$prov" = "custom" ] && [[ "$url" == *"api.dgrid.ai"* ]]; then pass "모델: custom → api.dgrid.ai ($mdl)"; else fail "모델이 Dgrid로 연결되지 않음 (provider=${prov:-없음})" "STEP 03: hermes model → Custom endpoint → https://api.dgrid.ai/v1"; fi
if [ -n "$key" ]; then
  code=$(curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $key" https://api.dgrid.ai/v1/models)
  if [ "$code" = "200" ]; then pass "Dgrid 키 유효 (HTTP 200)"; else fail "Dgrid 응답 HTTP $code" "401이면 키 재발급 후 STEP 03. 429면 1분 뒤 재시도"; fi
else fail "Dgrid API 키 없음" "STEP 02 → 03"; fi
if grep -qE '^TELEGRAM_BOT_TOKEN=.{20,}' "$ENVF" 2>/dev/null; then pass "텔레그램 봇 토큰 저장됨"; else fail "텔레그램 봇 토큰 없음" "STEP 04: hermes gateway setup"; fi
if grep -qE '^TELEGRAM_ALLOWED_USERS=[0-9]' "$ENVF" 2>/dev/null; then pass "텔레그램 허용 사용자 ID 저장됨"; else fail "TELEGRAM_ALLOWED_USERS 없음" "@userinfobot 에서 내 ID 확인 후 STEP 04"; fi
if pgrep -f "hermes.*gateway" >/dev/null 2>&1 || hermes gateway status 2>/dev/null | grep -qiE "loaded|running|active"; then pass "게이트웨이 실행 중"; else fail "게이트웨이가 꺼져 있음" "hermes gateway  (창 하나를 켜 둔다)"; fi
echo "== 끝. 폰에서 봇에게 '안녕' 보내서 답이 오면 완료 =="
