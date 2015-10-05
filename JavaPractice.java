public class JavaPractice 
{


	/*
		Prints out odd numbers between 1 and 99
	*/
	public static void printOddNumbers()
	{
		for (int i = 1; i < 100; i += 2)
		{
			System.out.println(i);
		}
	}

	public static void main(String[] args)
	{
		printOddNumbers();
	}
}