##구현 기능
1. 회원가입
  - 이름, 이메일, 비밀번호 입력
  - 이메일 정규표현식
  - 비밀번호 정규표현식(최소 한개의 영문자 + 최소 한개의 숫자 + 최소 8자)
  - bcrypt를 사용하여 비밀번호 암호화
2. 로그인
  - 이메일, 비밀번호 입력
  - 이메일 중복 및 비밀번호 복호화하여 일치여부 확인
  - jwt 이용하여 토큰 발행 (만료기간 1일), 유저의 ID를 토큰에 저장
3. 가계부 작성
  - 금액, 금액 세부 내역, 필기장, url입력
  - url 입력받는 부분은 착각하고 잘못 생각하여 모델링 진행 -> 추후에 모델링 수정 예정
  - 데코레이터로 토큰에 입력된 유저의 ID 값을 받고 사용자에게 입렫받은 값과 함께 테이블 작성
4. 가계부 보기
  - 프론트로부터 user_id를 받고 해당하는 정보를 내보냄
5. 가계부 수정
  - 수정하고싶은 내용을 입력 (금액 or 금액세부내역 or 필기장)
  - 가계부(accountbook) ID를 받아서 해당하는 Row의 값을 수정
6. 가계부 삭제
  - 가계부(accountbook) ID를 받아서 해당하는 Row 삭제
  - 토큰을 통해 유저의 ID도 확인
7. 세부내용 링크 생성
  - 오래 고민해 보았지만 구현은 실패
  - Schedule나 timer를 사용해보았음
  - 추후에 기회가 생긴다면 다시 도전해볼 예정
8. Unit Test 작성
  - 가계부(accountbook)의 Post와 Get부분 Unit Test 구현
  - Token Unit Test 구현
  - 추후에 기회가 된다면 공부하여 모두 진행할 예정

시간에 쫓기다 보니 생각보다 디테일하지 못했고, 실수가 잦았다.
특히 과제의 목표가 효율적이고 확장 가능하게 만드는 것인데 비효율적이고, 확장이 불가능하게 개발을 하고 있다는 것을 느꼈다.
실력이 정말 많이 부족하다고 느꼈고 더욱 노력하는 계기가 될것 같다.
이런 좋은 기회를 주셔서 감사하다.
