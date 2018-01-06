let stack = require(../stack)

test('Test there is no data on initialization', () => {
    let s = new stack.Stack();
    expect(s.head).toBeNull();
});

test('Test push method works', () => {
    let s = new stack.Stack();
    s.push(25)
    s.push(50)
    expect(s.head.val).toBe(50)
    expect(s.head.next.val)toBe(25)
});

test('Test pop method works', () => {
    let s = new stack.Stack();
    s.push(25)
    s.push(50)
    s.push(75)
    expect(s.pop()).toBe(25)
})

test('Test multiple pops', () => {
    let s = new stack.Stack();
    s.push(25)
    s.push(50)
    s.push(75)
    expect(s.pop()).toBe(25)
    expect(s.pop()).toBe(50)
})

test('Test peek method works', () => {
    let s = new stack.Stack();
    s.push(25)
    s.push(50)
    s.push(75)
    expect(s.peek()).toBe(75)
})