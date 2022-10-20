let N = 1

while (N < 10){
  let m = (N-1) / 2
  for (let i = m; i === 1; i--) {
    console.log(' ')
  }
  for (let j = 1; j === N; j++) {
    console.log('*')
  }
  console.log('\n')
  N += 2
}
