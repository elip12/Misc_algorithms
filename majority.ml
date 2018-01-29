(* 
    OCaml program for getting the majority element in a list, using bayer-moore algorithm
    Eli Pandolfo

    runs in O(n), where n is the length of the list (T(n) = 2n). makes one passto identify a candidate,
    then another pass to determine whether this is actually a majority element. All functions
    use tail recursion for O(1) stack space.

    print_maj takes in a list and outputs either 'Empty list', 'No majority element found',
    or 'Majority element: X'.

    maj takes in a list and uses the boyer-moore algorithm to identify a candidate for
    the majority element. It will always output a number, but that number will not be
    the majority element if none exists.

    is_maj takes in a list and a candidate and outputs true or false if the element is
    actually the majority element.
*)


let maj l =
    (* tail recursive worker fcn w/ accumulator to allow O(1) stack space *)
    let rec maj_ l_ count element =
        if (List.length l_) = 0 then
            element
        else if count = 0 then
            maj_ (List.tl l_) 1 (List.hd l_)
        else if element = (List.hd l_) then
            maj_ (List.tl l_) (count + 1) element
        else
            maj_ (List.tl l_) (count - 1) element in
    (* 'in' keyword allows the worker fcn to be called in subsequent lines until
        ';;' indicates end of code block. The worker fcn is the last thing called in
        the outer fcn, for tail recursion. *)
    maj_ l 0 0;;        
    
let is_maj l element =
    (* worker fcn. counts all occurences of element in list, and checks
        whether there are more than n/2 occurences. *)
    let rec is_maj_ l_ element_ count length =
        if (List.length l_) = 0 then
            if count > (length / 2) then
                true
            else
                false
        else if (List.hd l_) = element_ then
            is_maj_ (List.tl l_) element_ (count + 1) length
        else
            is_maj_ (List.tl l_) element_ count length in 
    is_maj_ l element 0 (List.length l);;

let print_maj l =
    (* checks for empty list, then runs both helper functions to determine
        whether a majority element exists and what it is *)
    if (List.length l) = 0 then
        print_string "Empty list\n"
    else
        let majority_element = maj l in
        if is_maj l majority_element = true then
            begin
                print_string "Majority element: ";
                print_int majority_element;
                print_string "\n";
            end
        else
            print_string "No majority element exists\n";;

