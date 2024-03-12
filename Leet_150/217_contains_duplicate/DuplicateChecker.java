import java.util.Arrays;
import java.util.Scanner;

public class DuplicateChecker {
    public static boolean containsDuplicate(int[] num) {
        Arrays.sort(num); // this sorts the array
        // check adjacent elements for duplicate
        for (int i = 0; i < num.length - 1; i++) {
            if (num[i] == num[i + 1]) {
                return true;// duplicate found
            }
        }
        return false;// No ducplicate found

    }

    public static void main(String[] args) {
        // getting no of elements from user
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements:");
        int n = sc.nextInt();
        // storing the array elements from user
        int num[] = new int[n];
        System.out.print("INPUT: ");
        for (int i = 0; i < n; i++) {
            num[i] = sc.nextInt();
        }

        boolean hasDuplicate = containsDuplicate(num);

        // Print the result
        if (hasDuplicate) {
            System.out.print("OUTPUT: true");
        } else {
            System.out.print("OUTPUT: false");
        }
        sc.close();
    }
}