using System;
using System.text;


public static class lockExample{
    private static readonly Random rnd = new Random(Guid.NewGuid().GetHashCode());
		private static readonly String[] ntv = { "6.0", "6.1", "6.2", "6.3", "10.0" };

		public static string RandomString(int length = 6)
		{
			StringBuilder builder = new StringBuilder();

			lock (rnd)
			{
				char ch;
				for (int i = 0; i < length; i++)
				{
					ch = Convert.ToChar(Convert.ToInt32(Math.Floor(26 * rnd.NextDouble() + 65)));
					builder.Append(ch);
                    Console.WriteLine(ch);
				}
			}

			return builder.ToString();
}