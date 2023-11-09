import axios from "axios";

export const getReplyFromQn = async (qn: string) => {
  const res = await axios.get("http://127.0.0.1:5000/api", {
    params: {
      prompt: qn,
    },
  });
  console.log(res.data);
  return res.data;
};

export const saveMessages = (messages: Message[]) => {
  localStorage.setItem("messages", JSON.stringify(messages));
};

export interface Message {
  message: string;
  isUser: boolean;
}
export interface Recipe {
  opening: string;
  title: string;
  ingredients: string;
  duration: string;
  steps: string;
  ending: string;
}

export const getRecipe = (recipeText: string) => {
  const sections = recipeText.split("\n\n");

  // Extract and parse the ingredients section
  const ingredientsSection = sections.find((section) =>
    section.startsWith("| Ingredient | Quantity |")
  );
  if (ingredientsSection) {
    const ingredientsData = ingredientsSection
      .split("\n")
      .slice(2) // Skip the header row and separator
      .map((row) => {
        const [ingredient, quantity] = row
          .split("|")
          .map((cell) => cell.trim());
        return { ingredient, quantity };
      });
    return ingredientsData;
  }
};
