
-- figuring out user country information through their ipaddresses

DROP TABLE IF EXISTS user_countryy;
CREATE TABLE `user_countryy` (
  `UserID` varchar(100) NOT NULL,
  `Contents` json,
  `IpAddress` char(100),
  `IpNumeric` double,
  `Country` char(10),
  `PlayCount` int,					-- 게임 횟수
  `DepositCount` int,				-- 입금 횟수
  `dep_usd` decimal (20,3),			-- 입금액
  `bet_usd` DECIMAL(20,3),			-- 베팅 총액

  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
-- select UserID, contents from Ticket where timestamp >= '2019-05-01' group by UserID;
insert into user_countryy (UserID, Contents)
select UserID, contents from Ticket
where timestamp >= '2019-05-01' group by UserID;

update user_countryy set IpAddress = json_unquote(json_extract(Contents, '$.ipAddress'));

-- delete from
select * from user_countryy where IpAddress = "";			-- 불순물 제거, IpAddress 가 없는 놈
select * from user_countryy where length(IpAddress) > 15;		-- 불순물 제거, IpAddress 가 두 개인 놈

select * from user_countryy;

update user_countryy set IpNumeric = inet_aton(json_unquote(IpAddress));
-- Error Code: 1411. Incorrect string value: '`rocket`.`user_countryy`.`IpAddress`' for function inet_aton

select * from user_countryy;

update user_countryy inner join IpCountry
	on user_countryy.IpNumeric between IpCountry.From and IpCountry.To
    set user_countryy.Country = IpCountry.Country;


select P.country, sum(P.countt) from(
select monthh, dayy, count(K.UserID) as countt, K.country from(
select U.country, U.UserID, month(R.CreatedAt) as monthh, day(R.CreatedAt) as dayy from user_countryy U join
User R on
U.UserID = R.ID
where country in
("TH", "MY", "ID", "VN")) as K
where K.UserID in (select UserID from Ticket where day(timestamp) = K.dayy
and month(timestamp) = K.monthh)
group by country, monthh, dayy) as P
where P.monthh >= 5
group by P.country
order by sum(P.countt) desc;

select * from ipcountry order by ipcountry.to desc;

select monthh, dayy, count(K.UserID) as countt, K.country from(
select U.country, U.UserID, month(R.CreatedAt) as monthh, day(R.CreatedAt)
as dayy from user_countryy U join
User R on
U.UserID = R.ID) as K
group by country, monthh, dayy;

select sum(hm) from (
select U.country, count(U.UserID) as hm from user_country U
group by country
order by count(U.UserID) desc) as K;

select count(*) from user_country;

select min(createdat), max(createdat), timediff(min(createdat), max(createdat)) from User where createdat >= "2019-05-01";

-- 가입자
select U.country, count(U.UserID) from user_countryy U join User R
on U.UserID = R.ID
where R.createdAt >= "2019-07-01" and R.createdat < "2019-08-01"
group by U.country
order by count(U.UserID) desc;

-- 액티브 유저
select U.country, count(distinct(U.UserID)) from user_countryy U join CoinHistory C
on U.UserID = C.UserID
where C.timestamp >= "2019-06-01" and C.timestamp < "2019-07-01"
group by U.country
order by count(distinct(U.UserID)) desc;

-- 결제자
select U.country, count(distinct(C.UserID)) as ct from CoinHistory C
join user_country u
on u.userID = C.userid
where timestamp >= "2019-07-01" and timestamp < "2019-08-01"
and message = "deposit"
group by U.country
order by ct desc;

-- arppu
select country, avg(SumDeltaUSD), count(UserID) as ctt from (
SELECT
	B.UserID, U.country, sum(J * C.Price->'$.usd' / POWER(10, C.`Precision`)) as SumDeltaUSD
from(select UserID, coin, timestamp, Delta as J
FROM CoinHistory where timestamp>='2019-05-01' AND timestamp<'2019-06-01'
and message='deposit') as B
Join Coin190527 as C on B.coin = C.ID
Join User_country U on U.UserID = B.UserID
group by B.UserID) as K
group by country
order by ctt desc;

select distinct(UserID) from CoinHistory where timestamp>='2019-05-01' AND timestamp<'2019-06-01'
and message='deposit';

select * from user_countryy;


select count(*) from User where createdat >= "2019-05-01";
