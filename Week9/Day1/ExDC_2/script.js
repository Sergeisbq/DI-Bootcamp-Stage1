
function allTruthy(...args) {
  let flag = true;

  args.forEach((item, i) => {
    if (item !== true) {
      flag = false;
    }
  });

  console.log(flag);
}

allTruthy(true, true, true);
allTruthy(true, false, true);
allTruthy(5,4,3,2,1,0);

