# [JAVA 8] Stream



## 스트림이란?

- 스트림은 자바 8 API에 새로 추가된 기능이다. 스트림을 이용하면 선언형으로 컬렉션 데이터를 처리할 수 있다.
-  스트림은 단 한 번만 탐색할 수 있으며, 다시 탐색하기 위해서는 새로운 스트림을 만들어야한다.
- Limit 연산을 사용하면 쇼트서킷이라는 기법에 의해 연산수가 줄어든다.
- filter와 map 연산의 경우 한 과정으로 병합된다.





#### filter

- 람다를 인수로 받아 스트림에서 특정 요소를 제외시킨다.



#### map

- 람다를 이용해서 한 요소를 다른 쇼오로 변환하거나 정보를 추출한다.



#### limit

- 정해진 개수 이상의 요소가 스트림에 저장되지 못하게 스트림 크기를 축소한다.



#### collect

- 스트림을 다른 형식으로 변환한다.



#### sorted

- 기본은 오름차순으로 정렬하며 안에 Comparator를 넣어주면 Comparator 기준으로 정렬해준다.



#### distinct

- 중복된 것을 제거해준다.



#### forEach

- 스트림의 각 요소를 소비하면서 람다 사용



#### count

- 스트림의 요소 개수를 반환



#### collect

- 스트림을 리듀스해서 리스트, 맵, 정수 형식의 컬렉션을 만든다.



#### flatMap

- 각 배열을 스트림이 아니라 스트림의 콘텐츠로 매핑한다.



#### allMatch, anyMatch, noneMatch, findFirst, findAny

- allMatch 모든 요소가 true 일 경우 true 반환
- anyMatch 하나라도 맞으면 true 반환
- noneMatch 모든 요소가 false이면 true 반환
- findFirst 처음으로 맞는 요소 반환(앞에 filter)
- findAny 맞는 요소 반환(앞에 filter)



#### findFirst vs findAny

- stream은 병렬적으로 연산하므로 굳이 처음것을 찾을 필요가 없을 경우 findAny가 권장됨



### takeWhile, dropWhile

- 정렬되어 있을 경우 takeWhile(d -> d.getA>100) 과 같이 사용하여 필터처럼 사용 가능하다. drop은 반대의 경우이다.



#### Reducing

- 모든 스트림 요소를 처리해서 값으로 도출하는 것을 만한다.



