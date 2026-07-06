# IS Job Market Map

미국 R1/R2 + 아시아(싱가포르·홍콩) 313개교 정보시스템(IS) 잡마켓 지도 +
실시간 채용(isjobs.xyz) 오버레이. 모바일에서 홈 화면에 추가해 앱처럼 사용.

- `index.html` — GitHub Pages로 서빙되는 자체 완결형 지도(빌드 산출물).
- `build_pages.py` — Dropbox의 `artifact.html`을 문서 래퍼(viewport + noindex)로
  감싸 `index.html`을 생성.
- `robots.txt` — 검색엔진 크롤링 차단(noindex와 함께 링크 미공유 시 검색 노출 안 됨).

## 업데이트

주간 루틴(`update_jobs.py`)이 채용 데이터를 재수집·재빌드한 뒤:

```
python3 build_pages.py
git commit -am "update $(date +%F)" && git push
```

를 실행하면 같은 Pages URL에 최신본이 배포됨.
