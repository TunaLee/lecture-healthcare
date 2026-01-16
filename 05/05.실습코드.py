patients = [] 

def show_menu():
    print("\n====== 환자 정보 관리 ======")
    print("1) 환자 등록")
    print("2) 환자 목록 보기")
    print("3) 이름으로 검색")
    print("4) 메모 수정")
    print("5) 환자 삭제")
    print("6) 간단 통계 보기")
    print("7) 데이터 초기화")
    print("0) 종료")
    print("===========================")

def input_patient():
    name = input("이름: ").strip()
    age_text = input("나이(숫자): ").strip()
    gender = input("성별(M/F): ").strip().upper()
    memo = input("메모(선택): ").strip()

    if not age_text.isdigit():
        print("❌ 나이는 숫자로 입력하세요.")
        return
    if gender not in ("M", "F"):
        print("❌ 성별은 M 또는 F 로 입력하세요.")
        return

    age = int(age_text)
    patient = {"name": name, "age": age, "gender": gender, "memo": memo}
    patients.append(patient)
    print("✅ 등록 완료!")

def show_list():
    if not patients:
        print("목록이 비어 있습니다.")
        return
    print("\n[ 환자 목록 ]")
    for idx, p in enumerate(patients, start=1):
        print(f"{idx}. {p['name']} | {p['age']}세 | {p['gender']} | 메모:{p['memo'] or '-'}")

def search_by_name():
    if not patients:
        print("목록이 비어 있습니다.")
        return
    key = input("검색할 이름(부분일치): ").strip()
    matches = [p for p in patients if key in p["name"]]
    if not matches:
        print("검색 결과가 없습니다.")
        return
    print("\n[ 검색 결과 ]")
    for idx, p in enumerate(matches, start=1):
        print(f"{idx}. {p['name']} | {p['age']}세 | {p['gender']} | 메모:{p['memo'] or '-'}")

def edit_memo():
    if not patients:
        print("목록이 비어 있습니다.")
        return
    show_list()
    no = input("메모를 수정할 환자 번호: ").strip()
    if not no.isdigit():
        print("❌ 번호는 숫자입니다.")
        return
    no = int(no)
    if not (1 <= no <= len(patients)):
        print("❌ 범위를 벗어난 번호입니다.")
        return
    new_memo = input("새 메모: ").strip()
    patients[no-1]["memo"] = new_memo
    print("✅ 메모 수정 완료!")

def delete_patient():
    if not patients:
        print("목록이 비어 있습니다.")
        return
    show_list()
    no = input("삭제할 환자 번호: ").strip()
    if not no.isdigit():
        print("❌ 번호는 숫자입니다.")
        return
    no = int(no)
    if not (1 <= no <= len(patients)):
        print("❌ 범위를 벗어난 번호입니다.")
        return
    removed = patients.pop(no-1)
    print(f"✅ 삭제 완료: {removed['name']}")

def show_stats():
    n = len(patients)
    print("\n[ 간단 통계 ]")
    print(f"- 총 환자 수: {n}")
    if n == 0:
        print("- 평균 나이: 0")
        print("- 성별 분포: M=0, F=0")
        return
    avg_age = sum(p["age"] for p in patients) / n
    m_count = sum(1 for p in patients if p["gender"] == "M")
    f_count = n - m_count
    print(f"- 평균 나이: {avg_age:.1f}")
    print(f"- 성별 분포: M={m_count}, F={f_count}")

def clear_all():
    if not patients:
        print("이미 비어 있습니다.")
        return
    confirm = input("정말 초기화할까요? (Y/N): ").strip().upper()
    if confirm == "Y":
        patients.clear()
        print("✅ 전체 초기화 완료!")
    else:
        print("취소했습니다.")

# ===== 메인 루프 =====
while True:
    show_menu()
    cmd = input("메뉴 번호 선택: ").strip()

    if cmd == "1":
        input_patient()
        continue
    elif cmd == "2":
        show_list()
        continue
    elif cmd == "3":
        search_by_name()
        continue
    elif cmd == "4":
        edit_memo()
        continue
    elif cmd == "5":
        delete_patient()
        continue
    elif cmd == "6":
        show_stats()
        continue
    elif cmd == "7":
        clear_all()
        continue
    elif cmd == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("❌ 잘못된 입력입니다. 다시 선택하세요.")
        continue
