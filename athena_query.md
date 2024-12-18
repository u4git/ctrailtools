# CreateNetworkInterface

## 按 userAgent 分组，统计请求个数，

```
select count(*) as count, details.parsedEvent.userAgent from cloudtrailevents4json group by details.parsedEvent.userAgent
```

## 按 IAM Role 分组，统计请求个数，

```
select count(*) as count, details.parsedEvent.userIdentity.sessionContext.sessionIssuer.arn from cloudtrailevents4json group by details.parsedEvent.userIdentity.sessionContext.sessionIssuer.arn
```

## 按 IAM Role 分组，统计申请到的 IP 数，

```
select sum(t.count), t.arn from (select json_array_length(json_extract(details.parsedEvent.responseElements,'$.networkinterface.privateipaddressesset.item')) as count, details.parsedEvent.userIdentity.sessionContext.sessionIssuer.arn as arn from cloudtrailevents4json where details.parsedEvent.responseElements is not null) as t group by t.arn
```

## 统计分配的 IP 总数，

```
select sum(t.count) from (select json_array_length(json_extract(details.parsedEvent.responseElements,'$.networkinterface.privateipaddressesset.item')) as count, details.parsedEvent.requestID as requestID from cloudtrailevents4json where details.parsedEvent.responseElements is not null) as t
```


