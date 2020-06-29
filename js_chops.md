# Javascript JS

- [reducing functions](#functions)

*other cheatsheats*

- [LeCoupa](#https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/javascript.js)

## -> Functions

.map

```js
# return array of numbers of ids of all officers
var officersIds = officers.map(function (officer) {
  return officer.id
});

same as

const officersIds = officers.map(officer => officer.id);
```

.reduce basically summates things from an array

```js
const totalYears = pilots.reduce((acc, pilot) => acc + pilot.years, 0);
```

.filter()

```js
var rebels = pilots.filter(function (pilot) {
  return pilot.faction === "Rebels";
});
```
