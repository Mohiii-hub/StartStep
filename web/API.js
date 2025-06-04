const MEALDB_API_URL = "https://www.themealdb.com/api/json/v1/1";
console.log("API.js ERreisht")
const Randomrzept = document.getElementById("Randomrzept");
async function getMeal() {
    console.log("Getmeal API ist ausgefüllt")
    try {
        console.log("verbindung wird versucht")
        const Antwort = await fetch(`${MEALDB_API_URL}/random.php`);
        const Data = await Antwort.json();
        Randomrzept.innerText = Data.meals[0].strMeal.stringify();
        console.log("Datamels Class:",typeof Data.meals[0]);
        console.log(Data.meals[0].strMeal);
        console.log(Data.meals[0].strArea);
        console.log(Data.meals[0].strCategory);
        console.log(Data.meals[0].strIngredient1);
        console.log(Data.meals[0].strIngredient2);
        console.log(Data.meals[0].strIngredient3);
        console.log(Data.meals[0].strInstructions);

        console.log(Data.meals[0].strMealThumb);
    }
    catch (error) { console.error; }

}
getMeal();
async function getRandomMeals() {
    try {
        console.log('Fetching random meals...');
        const meals = [];
        // Fetch 6 random meals
        for (let i = 0; i < 6; i++) {
            console.log(`Fetching random meal ${i + 1}/6...`);
            const response = await fetch(`${MEALDB_API_URL}/random.php`);
            const data = await response.json();
            console.log(`Random meal ${i + 1} response:`, data);
            if (data.meals && data.meals[0]) {
                meals.push(data.meals[0]);
            }
        }
        console.log('All fetched meals:', meals);
        return meals;
    } catch (error) {
        console.error('Error fetching meals:', error);
        return [];
    }
}
getRandomMeals();
