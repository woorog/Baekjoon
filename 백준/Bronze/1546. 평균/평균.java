import java.util.Scanner;

public class Main {
	static Scanner scan = new Scanner(System.in);
	public static void main(String[] args) {

		
		int N=scan.nextInt();
		
		jax(N);

}

	private static void jax(int n) {
		int a[]=new int[n];
		double big=0;
		double avg=0;
		double avg1=0;
		for(int i=0;i<n;i++)
		{
			a[i]=scan.nextInt();
			if(a[i]>big)
			{
				big=a[i];
				
			}
			
		}
		
		for(int l=0;l<n;l++)
		{
			
			avg=a[l]/big*100;
			avg1+=avg;
			
			
			
		}
		avg1=avg1/n;
		System.out.println((double)Math.round(avg1*100)/100);
		
		
		
		
		
	}
	
}
