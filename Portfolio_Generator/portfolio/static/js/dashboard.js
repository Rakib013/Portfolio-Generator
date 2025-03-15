// DOM Elements
const menuToggle = document.getElementById('menu-toggle');
const sidebar = document.getElementById('sidebar');
const sidebarOverlay = document.getElementById('sidebar-overlay');
const contextMenu = document.getElementById('context-menu');
const portfolioItems = document.querySelectorAll('.portfolio-item:not(.create-new)');
const createNewBtn = document.getElementById('create-new-btn');
const createDialog = document.getElementById('create-dialog');
const dialogClose = document.getElementById('dialog-close');
const cancelBtn = document.getElementById('cancel-btn');
const createBtn = document.getElementById('create-btn');

const templateOptions = document.querySelectorAll('.template-option');
const previewPlaceholder = document.getElementById('preview-placeholder');
const templatePreviews = document.querySelectorAll('.template-preview-img');
const templateGalleryItems = document.querySelectorAll('.templates-section .portfolio-item');

// Preview Dialog Elements
const previewDialog = document.getElementById('preview-dialog');
const previewDialogClose = document.getElementById('preview-dialog-close');
const previewCloseBtn = document.getElementById('preview-close-btn');
const previewUseTemplateBtn = document.getElementById('preview-use-template-btn');
const previewTemplateTitle = document.getElementById('preview-template-title');
const previewTemplateImg = document.getElementById('preview-template-img');
const previewTemplateDescription = document.getElementById('preview-template-description');

// User Template Preview Dialog Elements
const userTemplatePreviewDialog = document.getElementById('user-template-preview-dialog');
const userTemplatePreviewClose = document.getElementById('user-template-preview-close');
const userTemplatePreviewCloseBtn = document.getElementById('user-template-preview-close-btn');
const userTemplateDownloadBtn = document.getElementById('user-template-download-btn');
const userTemplateDeleteBtn = document.getElementById('user-template-delete-btn');
const userTemplatePreviewTitle = document.getElementById('user-template-preview-title');
const userTemplatePreviewImg = document.getElementById('user-template-preview-img');
const userTemplatePreviewDescription = document.getElementById('user-template-preview-description');

// Toggle sidebar
menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('active');
    if (sidebar.classList.contains('active')) {
        sidebarOverlay.style.display = 'block';
        setTimeout(() => {
            sidebarOverlay.style.opacity = '1';
        }, 10);
    } else {
        sidebarOverlay.style.opacity = '0';
        setTimeout(() => {
            sidebarOverlay.style.display = 'none';
        }, 300);
    }
});

sidebarOverlay.addEventListener('click', () => {
    sidebar.classList.remove('active');
    sidebarOverlay.style.opacity = '0';
    setTimeout(() => {
        sidebarOverlay.style.display = 'none';
    }, 300);
});

// Context menu functionality
portfolioItems.forEach(item => {
    item.addEventListener('contextmenu', (e) => {
        e.preventDefault();
        const rect = item.getBoundingClientRect();
        const x = e.clientX;
        const y = e.clientY;
        
        // Position context menu
        contextMenu.style.left = `${x}px`;
        contextMenu.style.top = `${y}px`;
        
        // Show context menu
        contextMenu.classList.add('active');
        
        // Add data attribute to context menu
        contextMenu.dataset.targetId = item.dataset.id;
    });
    
    // Open on double click
    item.addEventListener('dblclick', () => {
        console.log(`Opening portfolio ${item.dataset.id}`);
        // Here you would redirect to the editor page or open the portfolio
        window.location.href = `editor.html?id=${item.dataset.id}`;
    });
});

// Hide context menu when clicking elsewhere
document.addEventListener('click', () => {
    contextMenu.classList.remove('active');
});

// Create new dialog
createNewBtn.addEventListener('click', () => {
    createDialog.classList.add('active');
});

function closeDialog() {
    createDialog.classList.remove('active');
    // Reset template selection and preview when closing dialog
    previewPlaceholder.style.display = 'block';
    createBtn.disabled = true;
    selectedTemplate = null;
    templateOptions.forEach(opt => opt.classList.remove('selected'));
}

dialogClose.addEventListener('click', closeDialog);
cancelBtn.addEventListener('click', closeDialog);

// Template selection and preview functionality
let selectedTemplate = null;

templateOptions.forEach(option => {
    option.addEventListener('click', () => {
        // Update selected class
        templateOptions.forEach(opt => opt.classList.remove('selected'));
        option.classList.add('selected');
        
        // Get template type
        selectedTemplate = option.dataset.template;
        
        // Update preview image
        templatePreviews.forEach(preview => preview.classList.remove('active'));
        const previewImg = document.getElementById(`preview-template${selectedTemplate}`);
        if (previewImg) {
            previewImg.classList.add('active');
            previewPlaceholder.style.display = 'none';
        }
        
        // Enable create button
        createBtn.disabled = false;
    });
});

// Template preview dialog functionality
function openPreviewDialog(templateId, templateName, templateDescription) {
    // Set the template title
    previewTemplateTitle.textContent = templateName || 'Template Preview';
    
    // Set the template image source
    const templateItem = document.querySelector(`.templates-section .portfolio-item[data-id="template${templateId}"]`);
    const templateImg = templateItem.querySelector('img');
    if (templateImg) {
        previewTemplateImg.src = templateImg.src;
    } else {
        previewTemplateImg.src = "{% static 'images/portfolio.png' %}";
    }
    
    // Set the template description
    previewTemplateDescription.textContent = templateDescription || 'No description available for this template.';
    
    // Get the URL from the data attribute and set it to the link
    if (templateItem && templateItem.dataset.url) {
        previewUseTemplateBtn.href = templateItem.dataset.url;
    }
    
    // Show the dialog
    previewDialog.classList.add('active');
}

function closePreviewDialog() {
    previewDialog.classList.remove('active');
}

// User Template preview dialog functionality
function openUserTemplatePreviewDialog(portfolioId, portfolioTitle, portfolioImg) {
    // Set the portfolio title
    userTemplatePreviewTitle.textContent = portfolioTitle || 'Portfolio Preview';
    
    // Set the portfolio image source
    userTemplatePreviewImg.src = portfolioImg;
    
    // Set the download URL
    userTemplateDownloadBtn.href = `/portfolio/download/${portfolioId}/`;
    userTemplateDeleteBtn.href = `/portfolio/delete/${portfolioId}/`;
    // Show the dialog
    userTemplatePreviewDialog.classList.add('active');
}

function closeUserTemplatePreviewDialog() {
    userTemplatePreviewDialog.classList.remove('active');
}

// Get user template items
const userTemplateItems = document.querySelectorAll('.recent-section .portfolio-item:not(.create-new)');

// Add event listeners to user template items
userTemplateItems.forEach(item => {
    item.addEventListener('click', (e) => {
        // Only capture the regular click, not the double click
        if (e.detail === 1) {
            // Wait a bit to see if it's going to be a double-click
            setTimeout(() => {
                if (!e.target.dblclick_handled) {
                    // Extract portfolio data
                    const portfolioId = item.dataset.id;
                    const portfolioTitle = item.querySelector('.portfolio-title').textContent;
                    const portfolioImg = item.querySelector('img').src;
                    
                    // Open the preview dialog
                    openUserTemplatePreviewDialog(portfolioId, portfolioTitle, portfolioImg);
                }
            }, 200);
        }
    });
    
    // Add tracking flag for double-click (maintain existing functionality)
    item.addEventListener('dblclick', (e) => {
        e.target.dblclick_handled = true;
        
        // Reset the flag after a short delay
        setTimeout(() => {
            e.target.dblclick_handled = false;
        }, 300);
    });
});

// Add event listeners to template gallery items
templateGalleryItems.forEach(item => {
    // Add click event for template preview
    item.addEventListener('click', (e) => {
        // Only capture the regular click, not the double click
        if (e.detail === 1) {
            // Wait a bit to see if it's going to be a double-click
            setTimeout(() => {
                if (!e.target.dblclick_handled) {
                    // Extract template data
                    const itemId = item.dataset.id;
                    const templateId = itemId.replace('template', '');
                    const templateName = item.dataset.name;
                    const templateDescription = item.dataset.description;
                    
                    // Open the preview dialog
                    openPreviewDialog(templateId, templateName, templateDescription);
                }
            }, 200);
        }
    });
    
    // Add tracking flag for double-click
    item.addEventListener('dblclick', (e) => {
        e.target.dblclick_handled = true;
        // Keep the existing functionality:
        // Extract the template ID for create dialog
        const itemId = item.dataset.id;
        const templateId = itemId.replace('template', '');
        
        // Open the create dialog
        createDialog.classList.add('active');
        
        // Auto-select the clicked template in the dialog
        const templateOption = document.querySelector(`.template-option[data-template="${templateId}"]`);
        if (templateOption) {
            // Simulate a click on the corresponding template option
            templateOption.click();
        }
        
        // Reset the flag after a short delay
        setTimeout(() => {
            e.target.dblclick_handled = false;
        }, 300);
    });
});

// Preview dialog close buttons
previewDialogClose.addEventListener('click', closePreviewDialog);
previewCloseBtn.addEventListener('click', closePreviewDialog);

// "Use This Template" link in preview dialog
previewUseTemplateBtn.addEventListener('click', () => {
    // Close the preview dialog - the link will handle the navigation
    closePreviewDialog();
});

// User Template Preview dialog close buttons
userTemplatePreviewClose.addEventListener('click', closeUserTemplatePreviewDialog);
userTemplatePreviewCloseBtn.addEventListener('click', closeUserTemplatePreviewDialog);

// Create button
createBtn.addEventListener('click', () => {
    if (selectedTemplate) {
        console.log(`Creating new portfolio with template: ${selectedTemplate}`);
        // Here you would make an API call to your backend to create a new portfolio
        // Then redirect to the editor
        window.location.href = `editor.html?template=${selectedTemplate}`;
    }
});