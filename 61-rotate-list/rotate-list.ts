/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function rotateRight(head: ListNode | null, k: number): ListNode | null {

  let ans = head 
  let res = head
  let n = 0
if (!head) return null

  while (head){
  n += 1 
  head = head.next
  }

     k = k % n
  if (k === 0) return ans
    const reach = n - k
    let poi = 0
    let start = null
    let curr = ans  
while (curr){
    poi += 1
    if (poi == reach){
        start = curr.next
        curr.next = null
        break
    } else {
        curr = curr.next
    }
}let fin_ans = start
        let prev = null
    while(start){

        prev = start
        start = start.next
    }
    prev.next = res



  return fin_ans
};