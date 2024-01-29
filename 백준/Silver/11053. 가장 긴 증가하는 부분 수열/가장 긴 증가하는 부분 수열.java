import java.util.Scanner;
/*
최장 증가 부분 수열(LIS) 문제
탐색하려는 인덱스(위치)에 대해서 이전 위치들을 찾아나가면서 해당 값보다 작을 경우 재귀호출을 통해 탐색해나가면 된다.
 main 에서 LIS() 을 0~ N-1 까지 모든 값에 대하여 반드시 탐색해야 한다. 
 그래야 각각의 원소에 대한 부분 증가 수열을 모두 구할 수가 있다.
 */
public class Main {
	 

	static int[] seq;
	static Integer[] dp;
	
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		
		int N = in.nextInt();
		
		seq = new int[N];
		dp = new Integer[N];
		
		
		for(int i = 0; i < N; i++) {
			seq[i] = in.nextInt();
		}
		
		// 0 ~ N-1 까지 모든 부분수열 탐색 
		for(int i = 0; i < N; i++) {
			LIS(i);
		}
		
		int max = dp[0];
		// 최댓값 찾기 
		for(int i = 1; i < N; i++) {
			max = Math.max(max, dp[i]);
		}
		System.out.println(max);
	}
	
	
	static int LIS(int N) {
		
		// 만약 탐색하지 않던 위치의 경우 
		if(dp[N] == null) {
			dp[N] = 1;	// 1로 초기화 
			
			// N-1 부터 0까지중 N보다 작은 값들을 찾으면서 재귀호출. 
			for(int i = N - 1; i >= 0; i--) {
				if(seq[i] < seq[N]) {
					dp[N] = Math.max(dp[N], LIS(i) + 1);
				}
			}
		}
		return dp[N];
	}
}